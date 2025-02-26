# Copyright (c) 2025, GreyCube Technologies and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestLibrarySystem(FrappeTestCase):
    def test_article_creation(self):
        article = frappe.get_doc(
		    doctype = "Article",
			article_name = "Book 1",
			author = "Test Author"
        ).insert()
		
        self.assertEqual(article.article_name, "Book 1")    