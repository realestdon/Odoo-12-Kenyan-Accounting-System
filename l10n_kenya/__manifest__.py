# -*- encoding: utf-8 -*-

# Copyright (C) 2019 Dishon Kadoh (<dishon.kadoh@gmail.com>).

{
    'name': 'Odoo12 Kenya - Accounting',
    'version': '12.0.0.1',
    'category': 'Localization',
    'license': 'AGPL-3',
    'description': """
        Basic Kenyan Chart of Accounts localisation necessary to run Odoo in Kenya:
        ================================================================================
        * A generic chart of accounts
        * Defines templates for sale and purchase VAT
        * Defines tax templates
   """,
    'author': 'Dishon Kadoh',
    'website': 'https://rottalsolutions.com',
    'depends': ['account', 'base_vat'],
    'data': [
        'data/account.account.tag.csv',
        'data/account.tax.group.csv',
        'data/account_chart_template_data.xml',
        'data/account.account.template.csv',
        'data/account_tax_template_data.xml',
        'data/account_chart_template_post_data.xml',
        'data/account_chart_template_configure_data.xml',
    ],
}
