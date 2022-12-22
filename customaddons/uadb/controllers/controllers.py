# -*- coding: utf-8 -*-
# from odoo import http


# class Uadb(http.Controller):
#     @http.route('/uadb/uadb', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uadb/uadb/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('uadb.listing', {
#             'root': '/uadb/uadb',
#             'objects': http.request.env['uadb.uadb'].search([]),
#         })

#     @http.route('/uadb/uadb/objects/<model("uadb.uadb"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uadb.object', {
#             'object': obj
#         })
