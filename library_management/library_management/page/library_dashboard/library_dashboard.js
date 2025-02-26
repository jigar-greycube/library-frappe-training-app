frappe.pages['library-dashboard'].on_page_load = function (wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'None',
		single_column: true
	});

	page.set_title("Library Dashboard")

	page.set_primary_action("Load JS Confetti", () => {
		frappe.require('library_dashboard.bundle.js', () => {
			console.log("JS Library Bundle Loaded")
		})
	})


	page.set_secondary_action("Load TSParticle Confetti", () => {
		frappe.require('library_tsparticles.bundle.js', () => {
			console.log("TS Library Bundle Loaded")
		})
	})
}