# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software.
# See LICENSE file for full copyright & licensing details.

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    internal_note = fields.Html('Note')
