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
    'name': 'EC Subscription Customs',
    'version': '16.0.1.0.4',
    'sequence': 12,
    'summary': 'EC Subscription Customs',
    'category': 'Sales',
    'website': '',
    'depends': [
        'account_move_customs',
        'sale_subscription',
    ],
    'data': [
        'views/sale_order_views.xml'
    ],
    'installable': True,
    'license': 'LGPL-3',
}
