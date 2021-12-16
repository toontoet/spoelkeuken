

import frappe
import spoelkeuken.utils

def scan_query(user):
    if not user:
        user = frappe.session.user
    # todos that belong to user or assigned by user
    organisation = spoelkeuken.utils.current_organisation()
    if not organisation:
    	return None 
    else:
    	return "(`tabScans`.organisation = {organisation})".format(organisation=frappe.db.escape(organisation))

def toets_query(user):

    if not user:
        user = frappe.session.user
    return None


def scan_has_permission(doc, user=None, permission_type=None):
    # when reading a document allow if event is Public
    # if permission_type == "read" and doc.event_type == "Public":
    #     return True

    # # when writing a document allow if event owned by user
    # if permission_type == "write" and doc.owner == user:
    #     return True

    print(doc)
    print (permission_type)
    print(user)
    return True
    #return False


def toets_has_permission(doc, user=None, permission_type=None):
    # when reading a document allow if event is Public
    # if permission_type == "read" and doc.event_type == "Public":
    #     return True

    # # when writing a document allow if event owned by user
    # if permission_type == "write" and doc.owner == user:
    #     return True

    print(doc)
    print (permission_type)
    print(user)
    return True
    #return False
