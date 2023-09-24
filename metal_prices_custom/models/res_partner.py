# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    billed_weight_quantity = fields.Float(string='Billed Weight Quantity', compute='_compute_billed_weight_quantity')

    def _compute_billed_weight_quantity(self):
        uom_category_weight = self.env.ref('uom.product_uom_categ_kgm')
        for partner in self:
            total_weight_quantity = 0.0
            for invoice in partner.invoice_ids:
                for line in invoice.invoice_line_ids:
                    if line.product_uom_id.category_id == uom_category_weight:
                        total_weight_quantity += line.quantity
            partner.billed_weight_quantity = total_weight_quantity


    def action_view_invoice(self):
        uom_category_weight = self.env.ref('uom.product_uom_categ_kgm')
        invoices = self.env['account.move'].search([
            ('partner_id', '=', self.id),
            ('invoice_line_ids.product_uom_id.category_id', '=', uom_category_weight.id),
        ])
        action = self.env.ref('account.action_move_out_invoice_type').read()[0]
        action['domain'] = [('id', 'in', invoices.ids)]
        return action
