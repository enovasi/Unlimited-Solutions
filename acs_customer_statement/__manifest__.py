# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'ACS Customer Statement',
    'summary': 'Adding Some features to Customer Statements report ',
    'category': 'Accounting',
    'description': """
Accounting Reports
==================
    This module adds Fiscal Position, Fiscal Date and Printer Serial number to Customer Statements report
    """,
    'category': 'Accounting',
    'author': 'Almighty Consulting Services',
    'support': 'info@almightycs.com',
    'website': 'http://www.almightycs.com',
    'depends': ['account','account_reports'],
    'data': ['views/account_invoice.xml'],
    'auto_install': False,
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4
