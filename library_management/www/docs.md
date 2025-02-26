---
base_template: templates/web.html
---
# Documentation

Welcome to Frappe Framework Documentation

Frappe, pronounced fra-pay, is a full stack, batteries-included, web framework written in Python and Javascript with MariaDB as the database. It is the framework which powers ERPNext, is pretty generic and can be used to build database driven apps.

{%- set articles = frappe.db.get_all("Article", '*') -%}

{% for article in articles %}
    **Article:** {{ article.article_name }},
    **Author:** {{ article.author }}, 
    **Status:** {{ article.status }}   
{% endfor %}