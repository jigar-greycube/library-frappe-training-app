// Copyright (c) 2025, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Article", {
    refresh(frm) {
        if (frm.doc.isbn) {
            frm.remove_custom_button();
        }

        frm.add_custom_button ('Fetch ISBN', () => {
            frm.call('set_isbn');
        })
    },
});

frappe.ui.form.on("Article Review", {
    reviews_add: function (frm, cdt, cdn) {
        console.log("Row Added", cdt, cdn)
    },
    reviews_remove: function (frm, cdt, cdn) {
        console.log("Row Removed", cdt, cdn)
    },
    reviews_move: function (frm, cdt, cdn) {
        console.log("Row Moved ", cdt, cdn)
    },
    form_render: function (frm, cdt, cdn) {
        console.log("Child Table Form Rendered", cdt, cdn);
    }
});
