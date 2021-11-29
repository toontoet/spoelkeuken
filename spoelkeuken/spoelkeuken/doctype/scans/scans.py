# Copyright (c) 2021, PublicSpaces and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Scans(Document):
    def before_save(self):
        print ("ProjectEmployee3: before_save")
        print (frappe.get_roles(frappe.session.user))
        if 'Spoelkeuken Deelnemer' in frappe.get_roles(frappe.session.user):

            self.organisation = 'VPRO'
        #print(self)
        #frappe.throw("before_save")