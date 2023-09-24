# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountMoveInherit(models.Model):

    _inherit = 'account.move'

    today_metal_price = fields.Float(string="Today's Metal Price")

    @api.onchange('today_metal_price')
    def set_today_metal_price(self):
        today_date = fields.Date.today()
        metal_price_wizard = self.env['metal.price.wizard'].search([('date', '=', today_date)], limit=1)

        if metal_price_wizard:
            self.today_metal_price = metal_price_wizard.metal_price
        elif self.today_metal_price > 0:
            metal_price_wizard = self.env['metal.price.wizard'].create({
                "metal_price": self.today_metal_price,
                "date": today_date,
            })









class AccountMoveLine(models.Model):

    _inherit = 'account.move.line'

    metal_total = fields.Float(string="Total")

    @api.depends('metal_total', 'quantity', 'move_id.today_metal_price', 'product_id')
    def _compute_price_unit(self):
        for line in self:
            if line.product_id and line.product_id.uom_id.category_id.id == 2:
                # if line.product_id and line.product_id.uom_id.category_id.name == 'weight' and line.move_id.today_metal_price > 0:
                #     line.price_unit = line.price_unit + line.move_id.today_metal_price
                if line.metal_total > 0 and line.quantity > 0:
                    line.price_unit = (line.metal_total - line.tax_ids[0].amount) / line.quantity
                else:
                    if line.product_id and line.move_id.today_metal_price > 0:
                        line.price_unit = line.product_id.list_price + line.move_id.today_metal_price
                    else:
                        line.price_unit = line.product_id.list_price
            else:
                line.price_unit = line.product_id.list_price





    @api.onchange('metal_total', 'quantity')
    def _onchange_metal_total(self):
        if self.metal_total and not self.quantity:
            raise UserError('Quantity is required when entering a value in "Total".')
        # if self.product_id and self.move_id.today_metal_price > 0:
        #     self.price_unit = self.price_unit + self.move_id.today_metal_price
        # else:
        #     self.price_unit = self.product_id.list_price



