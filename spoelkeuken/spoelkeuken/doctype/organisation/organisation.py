# Copyright (c) 2021, PublicSpaces and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import spoelkeuken.utils

class Organisation(Document):
	def on_change(self):

		olddoc = self.get_doc_before_save()

		if self.status != olddoc.status:
			if self.status == 'Active':
				spoelkeuken.utils.update_org_score(self.name)

