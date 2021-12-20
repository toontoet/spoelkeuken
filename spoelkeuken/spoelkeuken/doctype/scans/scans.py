# Copyright (c) 2021, PublicSpaces and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import spoelkeuken.utils
import statistics

class Scans(Document):

    def before_save(self):
        #print ("ProjectEmployee3: before_save")
        #print (frappe.get_roles(frappe.session.user))
        userOrganiation = spoelkeuken.utils.current_organisation()

        if userOrganiation != None:
            self.organisation = userOrganiation

        if self.date == None: 
            self.date = frappe.utils.now()


       
        score_open = []
        score_transparent = []
        score_accountable = []
        score_souvereign  = []
        score_usercentric = []


        for tool in self.tools:
            tool.score_open         = spoelkeuken.utils.calc_score(tool, {"q_open_1","q_open_2","q_open_3"})
            tool.score_transparent  = spoelkeuken.utils.calc_score(tool, {"q_transparent_1","q_transparent_2","q_transparent_3","q_transparent_4","q_transparent_5","q_transparent_6"})
            tool.score_accountable  = spoelkeuken.utils.calc_score(tool, {"q_accountable_1","q_accountable_2","q_accountable_3","q_accountable_4","q_accountable_5","q_accountable_6"})
            tool.score_souvereign   = spoelkeuken.utils.calc_score(tool, {"q_souvereign_1","q_souvereign_2","q_souvereign_3","q_souvereign_4","q_souvereign_5"})
            tool.score_usercentric  = spoelkeuken.utils.calc_score(tool, {"q_usercentric_1","q_usercentric_2","q_usercentric_3","q_usercentric_4","q_usercentric_5"})
            tool.score              = spoelkeuken.utils.calc_mean(tool)

            if tool.score_open > -1:
                score_open.append( tool.score_open )
            if tool.score_transparent > -1:
                score_transparent.append( tool.score_transparent )
            if tool.score_accountable > -1:
                score_accountable.append( tool.score_accountable )
            if tool.score_souvereign > -1:
                score_souvereign.append( tool.score_souvereign )
            if tool.score_usercentric > -1:
                score_usercentric.append( tool.score_usercentric )

        
        self.score_open         = statistics.mean( score_open ) if  len(score_open) > 0 else -1
        self.score_transparent  = statistics.mean( score_transparent ) if len(score_transparent) > 0 else -1
        self.score_accountable  = statistics.mean( score_accountable ) if len(score_accountable) > 0 else -1
        self.score_souvereign   = statistics.mean( score_souvereign ) if len(score_souvereign) > 0 else -1
        self.score_usercentric  = statistics.mean( score_usercentric ) if len(score_usercentric) > 0 else -1
        # total:

        self.score              = spoelkeuken.utils.calc_mean(self)

    def on_change(self):

        if self.status != 'New':
            spoelkeuken.utils.update_org_score(self.organisation)
            spoelkeuken.utils.update_tools()

        frappe.website.render.clear_cache()