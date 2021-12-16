frappe.ready(function() {
	// bind events here
	frappe.web_form.handle_success = (doc) => {
		//console.log(doc)
		window.location = '/scans/details/'+doc.name
	}
})