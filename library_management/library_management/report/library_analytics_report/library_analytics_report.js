// Copyright (c) 2025, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.query_reports["Library Analytics Report"] = {
	"filters": [
		{
			"fieldname" : "name",
			"fieldtype" : "Link",
			"label"     : __("Library Transaction"),
			"options"   : "Library Transaction"
		},
		{
			"fieldname" : "article",
			"fieldtype" : "Link",
			"label"     : __("Article"),
			"options"   : "Article"
		},
	],

	formatter: function(value, row, column, data, default_formatter){
		if (column.fieldname == 'type'){
			if (value == "Issue"){
				return `<span class = "badge badge-danger p-2">${value}</span>`
			}
			return `<span class = "badge badge-success p-2">${value}</span>`
		}
		
		return value
	} ,
	
};
