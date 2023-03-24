# -*- coding: utf-8 -*-
# Part of Odoo, EC Internet, Aktiv Software.
# See LICENSE file for full copyright & licensing details.

# Author: Aktiv Software PVT. LTD.
# mail: odoo@aktivsoftware.com
# Copyright (C) 2015-Present Aktiv Software PVT. LTD.
# Contributions:
#   Aktiv Software:
#     - Isufi Kapasi

{
    'name': 'EC Internet Subscription Customs',
    'version': '16.0.1.0.0',
    'sequence': 12,
    'summary': 'Subscription Customs',
    'category': 'Sales',
    'website': '',
    'depends': [
        'eci_account_customs',
        'sale_subscription',
    ],
    'data': [
        'views/sale_order_views.xml'
    ],
    'installable': True,
    'license': 'LGPL-3',
}
