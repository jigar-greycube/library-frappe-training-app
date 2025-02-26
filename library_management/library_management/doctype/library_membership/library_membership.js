// Copyright (c) 2025, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Membership", {
	refresh(frm) {
        frm.add_custom_button("Load JS Confetti", () => {
            frappe.require('library_dashboard.bundle.js')
        })
	},
});
