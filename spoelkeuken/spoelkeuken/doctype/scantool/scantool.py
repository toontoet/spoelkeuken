# Copyright (c) 2021, PublicSpaces and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import spoelkeuken.utils

class ScanTool(Document):
	def before_save(self):

		print("On before save ScanTool")

		# self.score_open 		= spoelkeuken.utils.calc_score({"q_open_1","q_open_2","q_open_3"})
		# self.score_transparent  = spoelkeuken.utils.calc_score({"q_transparent_1","q_transparent_2","q_transparent_3","q_transparent_4","q_transparent_5","q_transparent_6"})
		# self.score_accountable  = spoelkeuken.utils.calc_score({"q_accountable_1","q_accountable_2","q_accountable_3","q_accountable_4","q_accountable_5","q_accountable_6"})
		# self.score_souvereign 	= spoelkeuken.utils.calc_score({"q_souvereign_1","q_souvereign_2","q_souvereign_3","q_souvereign_4","q_souvereign_5"})
		# self.score_usercentric 	= spoelkeuken.utils.calc_score({"q_usercentric_1","q_usercentric_2","q_usercentric_3","q_usercentric_4","q_usercentric_5"})

		# userOrganiation = spoelkeuken.utils.current_organisation()
		# if userOrganiation != None:
		# 	self.organisation = userOrganiation

	def on_update(self):
		print ("On Update ScanTool")
