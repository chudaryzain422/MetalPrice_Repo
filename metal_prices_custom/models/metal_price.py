# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models,_


class MetalPrice(models.Model):
    _name = 'metal.price.wizard'

    metal_price = fields.Float(string="Metal Price")
    date = fields.Date(string="Date", default=lambda self: fields.Datetime.today())

    def action_show_metal_prices(self):
        # # Check if a record with the same date already exists
        # existing_record = self.search([('date', '=', self.date)], limit=1)
        #
        # if existing_record:
        #     # If a record already exists for the same date, update it
        #     existing_record.write({'metal_price': self.metal_price})
        # else:
        #     # If no record exists for the same date, create a new one
        #     self.create({'metal_price': self.metal_price, 'date': self.date})

        return {
            'name': _('Metal Prices'),
            'view_mode': 'tree,form',
            'res_model': 'metal.price.wizard',
            'type': 'ir.actions.act_window',
            'domain': [],  # You can add a domain to filter records if needed
        }
