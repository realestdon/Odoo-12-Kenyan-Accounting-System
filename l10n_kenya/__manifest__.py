# -*- encoding: utf-8 -*-

# Copyright (C) 2019 Dishon Kadoh (<dishon.kadoh@gmail.com>).

{
    'name': 'Kenya - Accounting',
    'version': '1.0',
    'category': 'Localization',
    'description': """
        Basic Kenyan Chart of Accounts localisation necessary to run Odoo in Kenya:
   """,
    'author': 'Dishon Kadoh',
    'website': 'dishon.kadoh@gmail.com',
    'support': 'dishon.kadoh@gmail.com',
    'license': ' AGPL-3',
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
