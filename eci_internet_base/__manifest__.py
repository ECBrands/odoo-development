# -*- coding: utf-8 -*-
# Part of Odoo, Ec Internet
# See LICENSE file for full copyright & licensing details.

{
    "name": "EC Internet Base",
    "summary": "",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "",
    "depends": [
        "base",
        "l10n_us_check_printing"
    ],
    "installable": True,
    'data': [
        'report/print_check_bottom.xml',
        'report/print_check_middle.xml',
        'report/print_check.xml',
        'views/res_company_view.xml',
        'views/res_partner_view.xml'
    ],
}
