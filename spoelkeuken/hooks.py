from . import __version__ as app_version

app_name = "spoelkeuken"
app_title = "Spoelkeuken"
app_publisher = "PublicSpaces"
app_description = "De PublicSpaces Spoelkeuken"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "toon@toetenel.com"
app_license = "MIT"


website_route_rules = [
    {"from_route": "/scans/details/<name>", "to_route": "scans/details"},
    {"from_route": "/organisation/<name>", "to_route": "organisation"},
    {"from_route": "/tool/<name>", "to_route": "tool"},
]

# website_context = {
# 	"favicon": "/assets/erpnext/images/yourlogo",
# 	"splash_image": "/assets/erpnext/images/yourlogo"
# }

brand_html = '<div>Spoelkeuken</div>'

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/spoelkeuken/css/spoelkeuken.css"
# app_include_js = "/assets/spoelkeuken/js/spoelkeuken.js"

# include js, css files in header of web template
web_include_css = "/assets/spoelkeuken/css/spoelkeuken.css"
# web_include_js = "/assets/spoelkeuken/js/spoelkeuken.js"

# include custom scss in every website theme (without file extension ".scss")
website_theme_scss = "public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "homepage"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
#website_generators = ["Scans"]

# Installation
# ------------

# before_install = "spoelkeuken.install.before_install"
#after_install = "spoelkeuken.install.after_install"

fixtures = [
    # export all records from the Category table
    "Website Settings",
    "Website Content",
    {"dt": "Workflow", "filters": [["name", "like", "Spoelkeuken%"]]},
    {"dt": "Workflow State", "filters": [["workflow_state_name", "in", ["New","Active","Archived","Offline"]]]},
    {"dt": "Workflow Action Master", "filters": [["name", "in", ["Archive","Activeer","Disable"]]]}
]

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "spoelkeuken.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"Scans": "spoelkeuken.permissions.scan_query",
	"ToolToets": "spoelkeuken.permissions.toets_query",
}
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

has_permission = {
    "Scans": "spoelkeuken.permissions.scan_has_permission",
    "ToolToets": "spoelkeuken.permissions.toets_has_permission"
}

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"spoelkeuken.tasks.all"
# 	],
# 	"daily": [
# 		"spoelkeuken.tasks.daily"
# 	],
# 	"hourly": [
# 		"spoelkeuken.tasks.hourly"
# 	],
# 	"weekly": [
# 		"spoelkeuken.tasks.weekly"
# 	]
# 	"monthly": [
# 		"spoelkeuken.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "spoelkeuken.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "spoelkeuken.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "spoelkeuken.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"spoelkeuken.auth.validate"
# ]

