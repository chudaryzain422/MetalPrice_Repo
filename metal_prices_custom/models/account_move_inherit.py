# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountMoveInherit(models.Model):

    _inherit = 'account.move'

    today_metal_price = fields.Float(string="Today's Metal Price")

























class AccountMoveLine(models.Model):

    _inherit = 'account.move.line'

    metal_total = fields.Float(string="Total")

    @api.depends('metal_total', 'quantity', 'move_id.today_metal_price')
    def _compute_price_unit(self):
        for line in self:
            if line.metal_total and line.quantity:
                line.price_unit = (line.metal_total - line.price_subtotal) / line.quantity
            else:
                line.price_unit = line.price_subtotal

            if line.move_id.today_metal_price:
                line.price_unit += line.move_id.today_metal_price


    @api.onchange('metal_total', 'quantity')
    def _onchange_metal_total(self):
        if self.metal_total and not self.quantity:
            raise UserError('Quantity is required when entering a value in "Total".')



