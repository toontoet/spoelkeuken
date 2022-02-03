


import frappe
import spoelkeuken.utils

def get_context(context):

	context.content = frappe.get_doc("Website Content")


	#'name': frappe.form_dict.name,

	if frappe.form_dict.category:

		context.category = frappe.get_doc("Category",frappe.form_dict.category)

		values = {'category': frappe.form_dict.category}
		tools = frappe.db.sql("""
		    SELECT
		        t.*
		    FROM `tabToolCategory` tc
		        LEFT JOIN `tabTool` t
		        ON tc.parent = t.name
		    WHERE  t.status = 'Active' AND tc.category = %(category)s
		    ORDER BY t.score DESC
		""", values=values, as_dict=1)

	else:

		context.category = False

		tools = frappe.db.get_all('Tool',
		    filters={
		      'status': 'Active'
		    },
		    fields= ["name","url","logo","description", "score","score_open","score_transparent","score_accountable","score_souvereign","score_usercentric"],
		    start=0, order_by='score desc'
		)

	context.tools = map(display_scores, tools)

	#context.title = context.tool.name;

	# values = {'tool': frappe.form_dict.name}
	# data = frappe.db.sql("""
	#     SELECT
	#         st.score,
	#         st.score_open,
	#         st.score_transparent,
	#         st.score_accountable,
	#         st.score_souvereign,
	#         st.score_usercentric,
	#         o.logo,
	#      	o.name
	#     FROM `tabScanTool` st
	#         LEFT JOIN `tabScans` s
	#         ON st.parent = s.name
	#         LEFT JOIN `tabOrganisation` o
	#         ON s.organisation = o.name
	#     WHERE s.status = 'Active' AND o.status = 'Active' AND st.tool = %(tool)s
	# """, values=values, as_dict=1)

	# context.orgs = map(display_scores, data)


	categories = frappe.db.sql("""
	    SELECT
	        tc.category, COUNT(*) as count
	    FROM `tabToolCategory` tc
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