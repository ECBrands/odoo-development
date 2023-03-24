# -*- coding: utf-8 -*-
# Part of Odoo, ECInternets, Aktiv Software.
# See LICENSE file for full copyright & licensing details.

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_note = fields.Html(string="Customer Note")

    def _prepare_invoice(self):
        """Override: Prepare Invoice Lines

        To Pass the Order Note to Invoice.

       :return: Super Call with updated res.
       """
        res = super(SaleOrder, self)._prepare_invoice()
        res['customer_note'] = self.customer_note
        return res
