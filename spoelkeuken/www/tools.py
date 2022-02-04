


import frappe
import spoelkeuken.utils

def get_context(context):

	context.content = frappe.get_doc("Website Content")


	#'name': frappe.form_dict.name,

	if frappe.form_dict.category:

		context.category = frappe.get_doc("Category",frappe.form_dict.category)

		context.title =  "Tools: " + frappe.form_dict.category;

		values = {'category': frappe.form_dict.category}
		tools = frappe.db.sql("""
		    SELECT
		        t.*,
		        COUNT(*) as scan_count
		    FROM `tabToolCategory` tc
		        LEFT JOIN `tabTool` t
		        ON tc.parent = t.name
		        LEFT JOIN `tabScanTool` st
		        ON st.tool = t.name
		        LEFT JOIN `tabScans` s
		        ON st.parent = s.name
		        LEFT JOIN `tabOrganisation` o
		        ON s.organisation = o.name
		    WHERE 
		    	o.status = 'Active' AND
		    	s.status = 'Active' AND 
		    	t.status = 'Active' AND 
		    	tc.category = %(category)s
		    GROUP BY t.name
		    ORDER BY t.score DESC
		""", values=values, as_dict=1)

	else:

		context.title =  "Alle tools"

		context.category = False

		tools = frappe.db.sql("""
		    SELECT
		        t.*,
		        COUNT(*) as scan_count
		    FROM `tabTool` t
		        LEFT JOIN `tabScanTool` st
		        ON st.tool = t.name
		        LEFT JOIN `tabScans` s
		        ON st.parent = s.name
		        LEFT JOIN `tabOrganisation` o
		        ON s.organisation = o.name
		    WHERE 
		    	o.status = 'Active' AND
		    	s.status = 'Active' AND 
		    	t.status = 'Active' 
		    GROUP BY t.name
		    ORDER BY t.score DESC
		""",  as_dict=1)

	context.tools = map(display_scores, tools)

	categories = frappe.db.sql("""
	    SELECT
	        tc.category, COUNT(DISTINCT(t.name)) as count
	    FROM `tabToolCategory` tc
		    LEFT JOIN `tabTool` t
	        ON tc.parent = t.name
	        LEFT JOIN `tabScanTool` st
	        ON st.tool = t.name
	        LEFT JOIN `tabScans` s
	        ON st.parent = s.name
	        LEFT JOIN `tabOrganisation` o
	        ON s.organisation = o.name
	    WHERE 
		    	o.status = 'Active' AND
		    	s.status = 'Active' AND 
		    	t.status = 'Active'
	    GROUP BY tc.category
	    ORDER by tc.name DESC
	""",  as_dict=1)

	
	context.categories = categories

def display_scores(row):

	row.score_class = class_score(row.score)
	row.score_open_class = class_score(row.score_open)
	row.score_transparent_class = class_score(row.score_transparent)
	row.score_accountable_class = class_score(row.score_accountable)
	row.score_souvereign_class = class_score(row.score_souvereign)
	row.score_usercentric_class = class_score(row.score_usercentric)

	row.score = display_score(row.score)
	row.score_open = display_score(row.score_open)
	row.score_transparent = display_score(row.score_transparent)
	row.score_accountable = display_score(row.score_accountable)
	row.score_souvereign = display_score(row.score_souvereign)
	row.score_usercentric = display_score(row.score_usercentric)

	
	return row


def display_score(score):
	if score < 0:
		return 'n.v.t.'
	else:
		return str(int(round(score*100,0))) +'%'

def class_score(score):
	if score < 0:
		return -1
	else:
		return int(round(score*10))