# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class MetalPrice(models.TransientModel):
    _name = 'metal.price.wizard'

    metal_price = fields.Float(string="Metal Price")
    date = fields.Date(string="Date", default=lambda self: fields.Datetime.today())