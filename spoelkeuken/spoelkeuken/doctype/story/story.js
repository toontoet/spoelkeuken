// Copyright (c) 2021, PublicSpaces and contributors
// For license information, please see license.txt

frappe.ui.form.on('Story', {

	refresh(frm) {
		// your code here
		if (!frm.doc.date) frm.set_value('date', frappe.datetime.now_datetime())
	}
});
