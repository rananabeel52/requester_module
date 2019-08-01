# -*- coding: utf-8 -*-

from odoo import http, SUPERUSER_ID
from odoo.http import request

class RequesterModule(http.Controller):

    @http.route(["/requests/new"], type='http', auth="public", methods=['GET', 'POST'], website=True)
    def request_new_fill_data(self, **kwargs):
        if request.httprequest.method == 'POST':
            print(kwargs)
            request.env['requester.module'].sudo().create({
                'req_name': kwargs.get('name'),
                'phone': kwargs.get('phone_number'),
                'email': kwargs.get('email'),
                'range': kwargs.get('range'),
                'person': kwargs.get('person'),
            })
        return request.render(
            "requester_module.sample_web_page", [])
