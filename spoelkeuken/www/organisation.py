


import frappe
import spoelkeuken.utils

def get_context(context):

	context.content = frappe.get_doc("Website Content")
	
	orgs = frappe.db.get_all('Organisation',
	    filters={
	      'name': frappe.form_dict.name,
	      'status': 'Active'
	    },
	    fields= ["name","url","logo","description","plan", "score","score_open","score_transparent","score_accountable","score_souvereign","score_usercentric"],
	    start=0,
	    page_length=1
	)

	if len(orgs) == 0:
		frappe.throw(_('Not Permitted'),frappe.PermissionError)
	else:
		context.org = orgs[0]

	context.title = context.org.name;

	values = {'org': frappe.form_dict.name}
	data = frappe.db.sql("""
	    SELECT
	        st.score,
	        st.score_open,
	        st.score_transparent,
	        st.score_accountable,
	        st.score_souvereign,
	        st.score_usercentric,
	        t.logo,
	     	t.name
	    FROM `tabScanTool` st
	        LEFT JOIN `tabTool` t
	        ON st.tool = t.name
	        LEFT JOIN `tabScans` s
	        ON st.parent = s.name
	    WHERE s.status = 'Active' AND t.status = 'Active' AND s.organisation = %(org)s
	""", values=values, as_dict=1)

	
	context.tools = map(display_scores, data)


	stories = frappe.db.sql("""
	    SELECT
	        s.url,
	     	s.title
	    FROM `tabStoryOrg` so
	        LEFT JOIN `tabStory` s
	        ON so.parent = s.name
	    WHERE so.organisation = %(org)s ORDER by s.date DESC
	""", values=values, as_dict=1)

	
	context.stories = stories

def display_scores(row):
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
