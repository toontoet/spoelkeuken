


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


	values = {'tool': frappe.form_dict.name}
	data = frappe.db.sql("""
	    SELECT
	        st.score,
	        o.logo,
	     	o.name
	    FROM `tabScanTool` st
	        LEFT JOIN `tabScans` s
	        ON st.parent = s.name
	        LEFT JOIN `tabOrganisation` o
	        ON s.organisation = o.name
	    WHERE s.status = 'Active' AND o.status = 'Active' AND st.tool = %(tool)s
	""", values=values, as_dict=1)

	context.orgs = data


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
