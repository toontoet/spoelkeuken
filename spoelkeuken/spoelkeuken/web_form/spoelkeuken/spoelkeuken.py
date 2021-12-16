from __future__ import unicode_literals

import frappe
from frappe import _
import spoelkeuken.utils

def get_context(context):
	# do your magic here
	if context.doc == '':
		# new document
		return


	org = spoelkeuken.utils.current_organisation()
	print (org)
	print(context.doc.organisation)
	if org != None:
		if org != context.doc.organisation:
			frappe.throw(_('Not Permitted'),frappe.PermissionError)