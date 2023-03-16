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
    'name': 'ECInternets Check Customisations',
    'version': '1.2',
    'summary': 'Invoice report',
    'sequence': 12,
    'description': "A",
    'category': 'Accounting',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': [
        'l10n_us_check_printing'
    ],
    'data': [
        'report/print_check_template.xml'
    ],
    'installable': True,
    'license': 'LGPL-3',
    'assets': {
        'web.report_assets_common': [
            'account_payment_checks_report/static/src/scss/report_check_middle.scss',
            'account_payment_checks_report/static/**/*',
        ],
    }
}
