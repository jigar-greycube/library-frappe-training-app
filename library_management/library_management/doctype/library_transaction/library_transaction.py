# Copyright (c) 2025, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe 								  
from frappe.model.document import Document    
from frappe.model.docstatus import DocStatus  


class LibraryTransaction(Document):
	def validate(self):
		self.validate_membership()

	def validate_issue(self):
		self.validate_membership()
		article = frappe.get_doc("Article", self.article)

		if article.status == "Issued":
			frappe.throw("Article is already issued by another member")

	def validate_return(self):

		article = frappe.get_doc("Article", self.article)

		if article.status == "Available":
			frappe.throw("Article can not be returned without being issued first")

	def before_save(self):
		if self.type == "Issue":
			self.validate_issue()

			article = frappe.get_doc("Article", self.article)
			article.status = "Issued"
			article.save()

		elif self.type == "Return":
			self.validate_return()
			
			article = frappe.get_doc("Article", self.article)
			article.status = "Available"
			article.save()

	def validate_membership(self):
		validate_membership = frappe.db.exists("Library Membership", {
			"library_member" : self.library_member,
			"docstatus": DocStatus.submitted(),
			"from_date" : ("<", self.date),
			"to_date": (">", self.date)
		})

		if not validate_membership:
			frappe.throw("The member does not have valid membership")

	def validate_maximum_limit(self):
		max_limit = frappe.db.get_single_value("Library Settings", "maximum_number_of_issued_articles")
		count  = frappe.db.count("Library Transaction", {
			"library_member" : self.library_member,
			"type" : "Issued",
			"docstauts" : DocStatus.submitted()
		})

		if count > max_limit:
			frappe.throw("Maximum limit is reached for issuing articles")