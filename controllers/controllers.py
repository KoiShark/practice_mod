# -*- coding: utf-8 -*-
# from odoo import http


# class PracticeMod(http.Controller):
#     @http.route('/practice_mod/practice_mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/practice_mod/practice_mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('practice_mod.listing', {
#             'root': '/practice_mod/practice_mod',
#             'objects': http.request.env['practice_mod.practice_mod'].search([]),
#         })

#     @http.route('/practice_mod/practice_mod/objects/<model("practice_mod.practice_mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('practice_mod.object', {
#             'object': obj
#         })
