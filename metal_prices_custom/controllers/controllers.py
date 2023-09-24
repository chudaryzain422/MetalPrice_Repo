# -*- coding: utf-8 -*-
# from odoo import http


# class MetalPricesCustom(http.Controller):
#     @http.route('/metal_prices_custom/metal_prices_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/metal_prices_custom/metal_prices_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('metal_prices_custom.listing', {
#             'root': '/metal_prices_custom/metal_prices_custom',
#             'objects': http.request.env['metal_prices_custom.metal_prices_custom'].search([]),
#         })

#     @http.route('/metal_prices_custom/metal_prices_custom/objects/<model("metal_prices_custom.metal_prices_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('metal_prices_custom.object', {
#             'object': obj
#         })
