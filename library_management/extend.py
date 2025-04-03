import frappe

def boot_session(bootinfo):
    bootinfo.library = {
        "articles" : "test_article"
    }

# def successful_login(login_manager):
#     print("Welcome to Frappe")