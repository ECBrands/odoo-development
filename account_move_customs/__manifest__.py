# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software.
# See LICENSE file for full copyright & licensing details.

# Author: Aktiv Software PVT. LTD.
# mail: odoo@aktivsoftware.com
# Copyright (C) 2015-Present Aktiv Software PVT. LTD.
# Contributions:
#   Aktiv Software:
#     - Isufi Kapasi

{
    'name': 'EC Internet Account Move Customs',
    'version': '15.0.1.0.0',
    'sequence': 12,
    'summary': 'Account Move Customs',
    'category': 'Accounting',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': [
        'account'
    ],
    'data': [
        'views/account_move_views.xml',
        'reports/report_invoice_document.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
