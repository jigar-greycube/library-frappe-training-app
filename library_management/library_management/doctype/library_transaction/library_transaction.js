// Copyright (c) 2025, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Transaction", {
	onload: function(frm) {
        frm.set_query('article', () => {
            return {
                filters: {
                    publisher: ['is', 'set'],
                    article_name: ['like', 'H%']
                }
            }
        })
    }
});
