# Copyright (c) 2025, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Article(WebsiteGenerator):
	@frappe.whitelist()
	def set_isbn(self):
		self.isbn = frappe.utils.generate_hash('Article', 10).upper()

	def get_article(self):
		return self.article_name
