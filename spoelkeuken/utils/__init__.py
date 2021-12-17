
import frappe
import statistics

def current_organisation():
	return None
	#p = frappe.db.get_value("User", frappe.session.user , ["organisation"], as_dict=True)
	#return p.organisation


def calc_score(scantool,  fields):
	num = 0
	score = 0;
	for f in fields:
		if getattr(scantool,f) != 'n/a':
			num = num + 1
		if getattr(scantool,f) == 'yes':
			score = score + 1
	if num == 0:
		return -1
	else:
		return score / num;

def calc_mean(scantool):

	return calc_valid_mean([scantool.score_open,scantool.score_transparent,scantool.score_accountable,scantool.score_souvereign,scantool.score_usercentric])

	#[self.score_open,self.score_transparent,self.score_accountable,self.score_souvereign,self.score_usercentric]

	# candidates = []
	# if scantool.score_open > -1:
	# 	candidates.append( scantool.score_open )
	# if scantool.score_transparent > -1:
	# 	candidates.append( scantool.score_transparent )
	# if scantool.score_accountable > -1:
	# 	candidates.append( scantool.score_accountable )
	# if scantool.score_souvereign > -1:
	# 	candidates.append( scantool.score_souvereign )
	# if scantool.score_usercentric > -1:
	# 	candidates.append( scantool.score_usercentric )

	# return statistics.mean(candidates)


def calc_valid_mean(scores):
	validScores = list(filter(lambda s: s>-1, scores))
	if len(validScores) == 0:
		return -1
	return statistics.mean(validScores)

def update_orgs_by_tool(tool):

	values = {'tool': tool}
	orgs = frappe.db.sql("""
		SELECT
			s.organisation
		FROM `tabScanTool` st
			LEFT JOIN `tabTool` t
			ON st.tool = t.name
			LEFT JOIN `tabScans` s
			ON st.parent = s.name
		WHERE st.tool = %(tool)s AND s.status = 'Active'
	""", values=values, as_dict=1)

	for org in orgs:
		update_org_score(org.organisation)



def update_org_score(org):

	score_open = []
	score_transparent = []
	score_accountable = []
	score_souvereign  = []
	score_usercentric = []

	values = {'org': org}
	scans = frappe.db.sql("""
		SELECT
			st.score,
			st.score_open,
			st.score_transparent,
			st.score_accountable,
			st.score_souvereign,
			st.score_usercentric
		FROM `tabScanTool` st
			LEFT JOIN `tabTool` t
			ON st.tool = t.name
			LEFT JOIN `tabScans` s
			ON st.parent = s.name
		WHERE s.status = 'Active' AND t.status = 'Active' AND s.organisation = %(org)s
	""", values=values, as_dict=1)


	for scan in scans:

		if scan.score_open > -1:
			score_open.append( scan.score_open )
		if scan.score_transparent > -1:
			score_transparent.append( scan.score_transparent )
		if scan.score_accountable > -1:
			score_accountable.append( scan.score_accountable )
		if scan.score_souvereign > -1:
			score_souvereign.append( scan.score_souvereign )
		if scan.score_usercentric > -1:
			score_usercentric.append( scan.score_usercentric )

	orgDoc = frappe.get_doc('Organisation', org);

	orgDoc.score_open         = statistics.mean( score_open ) if  len(score_open) > 0 else -1
	orgDoc.score_transparent  = statistics.mean( score_transparent ) if len(score_transparent) > 0 else -1
	orgDoc.score_accountable  = statistics.mean( score_accountable ) if len(score_accountable) > 0 else -1
	orgDoc.score_souvereign   = statistics.mean( score_souvereign ) if len(score_souvereign) > 0 else -1
	orgDoc.score_usercentric  = statistics.mean( score_usercentric ) if len(score_usercentric) > 0 else -1

	orgDoc.score              = calc_mean( orgDoc );

	orgDoc.save()


def update_tools():

	tools = frappe.db.get_all("Tool");
	for tool in tools:
		update_tool_score(tool.name)


def update_tool_score(tool):

	score_open = []
	score_transparent = []
	score_accountable = []
	score_souvereign  = []
	score_usercentric = []

	values = {'tool': tool}
	scans = frappe.db.sql("""
		SELECT
			st.score,
			st.score_open,
			st.score_transparent,
			st.score_accountable,
			st.score_souvereign,
			st.score_usercentric
		FROM `tabScanTool` st
			LEFT JOIN `tabTool` t
			ON st.tool = t.name
			LEFT JOIN `tabScans` s
			ON st.parent = s.name
		WHERE t.name = %(tool)s AND s.status = 'Active' AND t.status = 'Active'
	""", values=values, as_dict=1)

	print (tool)
	for scan in scans:
		print (scan.score_open)
		if scan.score_open > -1:
			score_open.append( scan.score_open )
		if scan.score_transparent > -1:
			score_transparent.append( scan.score_transparent )
		if scan.score_accountable > -1:
			score_accountable.append( scan.score_accountable )
		if scan.score_souvereign > -1:
			score_souvereign.append( scan.score_souvereign )
		if scan.score_usercentric > -1:
			score_usercentric.append( scan.score_usercentric )

	orgDoc = frappe.get_doc('Tool', tool);

	orgDoc.score_open         = statistics.mean( score_open ) if  len(score_open) > 0 else -1
	orgDoc.score_transparent  = statistics.mean( score_transparent ) if len(score_transparent) > 0 else -1
	orgDoc.score_accountable  = statistics.mean( score_accountable ) if len(score_accountable) > 0 else -1
	orgDoc.score_souvereign   = statistics.mean( score_souvereign ) if len(score_souvereign) > 0 else -1
	orgDoc.score_usercentric  = statistics.mean( score_usercentric ) if len(score_usercentric) > 0 else -1

	orgDoc.score              = calc_mean( orgDoc );


	# orgDoc.db_set('score_open', statistics.mean( score_open ) if  len(score_open) > 0 else -1)
	# orgDoc.db_set('score_transparent', statistics.mean( score_transparent ) if len(score_transparent) > 0 else -1)
	# orgDoc.db_set('score_accountable', statistics.mean( score_accountable ) if len(score_accountable) > 0 else -1)
	# orgDoc.db_set('score_souvereign', statistics.mean( score_souvereign ) if len(score_souvereign) > 0 else -1)
	# orgDoc.db_set('score_usercentric', statistics.mean( score_usercentric ) if len(score_usercentric) > 0 else -1)

	# orgDoc.db_set('score', calc_mean( orgDoc ))

	print(orgDoc.score)

	orgDoc.save()

