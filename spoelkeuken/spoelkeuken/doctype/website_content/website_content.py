# Copyright (c) 2021, PublicSpaces and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class WebsiteContent(Document):
	def on_change(self):

        frappe.website.render.clear_cache()
