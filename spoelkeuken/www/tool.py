


import frappe
import spoelkeuken.utils

def get_context(context):

	context.content = frappe.get_doc("Website Content")

	tools = frappe.db.get_all('Tool',
	    filters={
	      'name': frappe.form_dict.name,
	      'status': 'Active'
	    },
	    fields= ["name","url","logo","description", "score","score_open","score_transparent","score_accountable","score_souvereign","score_usercentric"],
	    start=0,
	    page_length=1
	)

	if len(tools) == 0:
		frappe.throw(_('Not Permitted'),frappe.PermissionError)
	else:
		context.tool = tools[0]

	context.title = context.tool.name;

	values = {'tool': frappe.form_dict.name}
	data = frappe.db.sql("""
	    SELECT
	        st.score,
	        st.score_open,
	        st.score_transparent,
	        st.score_accountable,
	        st.score_souvereign,
	        st.score_usercentric,
	        o.logo,
	     	o.name
	    FROM `tabScanTool` st
	        LEFT JOIN `tabScans` s
	        ON st.parent = s.name
	        LEFT JOIN `tabOrganisation` o
	        ON s.organisation = o.name
	    WHERE s.status = 'Active' AND o.status = 'Active' AND st.tool = %(tool)s
	""", values=values, as_dict=1)

	context.orgs = map(display_scores, data)


	stories = frappe.db.sql("""
	    SELECT
	        s.url,
	     	s.title
	    FROM `tabStoryTool` st
	        LEFT JOIN `tabStory` s
	        ON st.parent = s.name
	    WHERE st.tool = %(tool)s ORDER by s.date DESC
	""", values=values, as_dict=1)

	
	context.stories = stories

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