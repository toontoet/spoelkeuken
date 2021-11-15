# Copyright (c) 2021, PublicSpaces and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AssessmentTool(Document):

	def before_save(self):
		self.score_open 		= self.calc_score({"q_open_1","q_open_2","q_open_3"})
		self.score_transparent  = self.calc_score({"q_transparent_1","q_transparent_2","q_transparent_3","q_transparent_4","q_transparent_5","q_transparent_6"})
		self.score_accountable  = self.calc_score({"q_accountable_1","q_accountable_2","q_accountable_3","q_accountable_4","q_accountable_5","q_accountable_6"})
		self.score_souvereign 	= self.calc_score({"q_souvereign_1","q_souvereign_2","q_souvereign_3","q_souvereign_4","q_souvereign_5"})
		self.score_usercentric 	= self.calc_score({"q_usercentric_1","q_usercentric_2","q_usercentric_3","q_usercentric_4","q_usercentric_5"})

	def calc_score(self, fields):
		print 
		num = 0
		score = 0;
		for f in fields:
			if getattr(self,f) != 'n/a':
				num = num + 1
			if getattr(self,f) == 'yes':
				score = score + 1
		if num == 0:
			return 0
		else:
			return score / num;
