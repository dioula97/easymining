# -*- coding: utf-8 -*-
from odoo import http

# class Easymining(http.Controller):
#     @http.route('/easymining/easymining/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/easymining/easymining/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('easymining.listing', {
#             'root': '/easymining/easymining',
#             'objects': http.request.env['easymining.easymining'].search([]),
#         })

#     @http.route('/easymining/easymining/objects/<model("easymining.easymining"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('easymining.object', {
#             'object': obj
#         })