// Copyright (c) 2021, PublicSpaces and contributors
// For license information, please see license.txt

frappe.ui.form.on('Scans', {
	refresh(frm) {
		// your code here
		if (!frm.doc.date) frm.set_value('date', frappe.datetime.nowdate())
	}
})

frappe.ui.form.on('ScanTool', {
	form_render(frm, cdt, cdn) {
		// your code here

		[
			  "q_open_1_note",
			  "q_open_2_note",
			  "q_open_3_note",
			  "q_transparent_1_note",
			  "q_transparent_2_note",
			  "q_transparent_3_note",
			  "q_transparent_4_note",
			  "q_transparent_5_note",
			  "q_transparent_6_note",
			  "q_accountable_1_note",
			  "q_accountable_2_note",
			  "q_accountable_3_note",
			  "q_accountable_4_note",
			  "q_accountable_5_note",
			  "q_accountable_6_note",
			  "q_souvereign_1_note",
			  "q_souvereign_2_note",
			  "q_souvereign_3_note",
			  "q_souvereign_4_note",
			  "q_souvereign_5_note",
			  "q_usercentric_1_note",
			  "q_usercentric_2_note",
			  "q_usercentric_3_note",
			  "q_usercentric_4_note",
			  "q_usercentric_5_note"
		].forEach(field=>{

			/* resize textarea's */
			$(`textarea[data-fieldname="${field}"]`).css("height","75px");
			$(`textarea[data-fieldname="${field}"]`).css("resize","vertical");

			$(`textarea[data-fieldname="${field}"]`).keyup(function(e) {
			    while($(this).outerHeight() < this.scrollHeight + parseFloat($(this).css("borderTopWidth")) + parseFloat($(this).css("borderBottomWidth"))) {
			        $(this).height($(this).height()+1);
			    };
			});
		})

		



	}
})