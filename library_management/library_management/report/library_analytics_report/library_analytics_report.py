# Copyright (c) 2025, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	if not filters: filters = {}
	columns, data = [], []

	columns = get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data:
		frappe.msgprint("No Records Found")
		return columns, data
	
	for doc in cs_data:
		row = frappe._dict({
			"article" : doc.article,
			"type" : doc.type,
			"library_member" : doc.library_member
		})
		data.append(row)

	chart = get_chart(data)

	report_summary = get_report_summary(data)

	return columns, data, None, chart, report_summary


def get_columns():
	return [
		{
			"fieldname" : "article",
			"fieldtype" : "Link",
			"label" : "Article Name",
			"options": "Article",
			"width" : 230
		},
		{
			"fieldname" : "type",
			"fieldtype" : "Data",
			"label" : "Transaction Type",
			"width" : 230
 		},
		{
			"fieldname" : "library_member",
			"fieldtype" : "Data",
			"label" : "Library Member",
			"width" : 230
		}
	]

def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype = "Library Transaction",
		fields = ["article", "type", "library_member"],
		filters = conditions,
	)

	return data


def get_conditions(filters):
	conditions = {}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value
	

	return conditions

def get_chart(data):
	if not data:
		return None
	
	labels = ["Issued", "Returned"]


	transaction_data = {
		"Issued" : 0,
		"Returned" : 0
	}

	datasets = []

	for doc in data:
		if doc.type == "Issue":
			transaction_data["Issued"] += 1
		elif doc.type == "Return":
			transaction_data["Returned"] += 1

	datasets.append({
		"name" : "Transaction Status",
		"values" : [transaction_data.get("Issued"), transaction_data.get("Returned")]
	})

	chart = {
		"data" : {
			"labels" : labels,
			"datasets" : datasets
		},
		"type" : "bar",
		"height" : 100			
	}
	
	return chart

def get_report_summary(data):
	if not data:
		return None
	
	issued, returned = 0, 0

	for doc in data: 
		if doc.type == "Issue":
			issued += 1
		elif doc.type == "Return":
			returned += 1

	return [
		{
			"datatype": "Int",
			"label" : "Issued Articles",
			"value": issued,
			"indicator": "black"
		},
		{
			"type" : "separator",
			"value" : "+",
		},
		{
			"datatype": "Int",
			"label" : "Returned Articles",
			"value": returned,
			"indicator": "black"
		},
		{
			"type" : "separator",
			"value" : "=",
			"color" : "blue"
		},
		{
			"datatype": "Int",
			"label" : "Total Transactions",
			"value": len(data),
			"indicator": "green"
		}
	]