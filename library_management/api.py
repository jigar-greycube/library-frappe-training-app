import frappe
from frappe.auth import LoginManager

@frappe.whitelist(allow_guest=True)
def mobile_login(usr=None, pwd=None):
    if not usr or not pwd:
        frappe.throw("Missing username or password")
        
    login_manager = LoginManager()
    login_manager.authenticate(user=usr, pwd=pwd)
    login_manager.post_login()
    
    user = frappe.get_doc("User", frappe.session.user)
    
    # generate API keys if not present
    if not user.api_key:
        user.api_key = frappe.generate_hash(length=15)
        user.api_secret = frappe.generate_hash(length=15)
        user.save(ignore_permissions=True)
        
    return {
        "api_key": user.api_key,
        "api_secret": user.api_secret,
        "user": user.name,
        "full_name": user.full_name,
    }