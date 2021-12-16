
import frappe
import spoelkeuken.utils

def get_context(context):
	context.content = frappe.get_doc("Website Content")

	context.stories = frappe.db.get_all("Story",
			filters={
				'homepage': True,
			},
			fields= ["title","url","date"],
			order_by='date desc',
			page_length=10,
		)


	context.participants = frappe.db.get_all("Organisation",
			filters={
				'status': 'Active',
			},
			fields= ["name","logo"],
			order_by='name asc'
		)

	context.tools = frappe.db.get_all("Tool",
			filters={
				'status': 'Active',
			},
			fields= ["name","logo"],
			order_by='name asc',
			page_length=6,
		)


