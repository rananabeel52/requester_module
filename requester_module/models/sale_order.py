# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def _onchange_partner(self):
        if self.partner_id:
            data_list = []
            data_list.append({'product_id': 10,
                              'name': 'abc',
                              'product_uom_qty': 1,
                              'price_unit': 123,
                              # 'order_id': self.id
                              })
            print("dfgyui;oklkjhbv")
            self.update({'order_line': data_list})
        # print("ddddddddddddddddddddddddd", self.id)
        # # for line in self.partner_id.service_ids:
        # data = self.order_line.create({
        #     'product_id': 10,
        #     'name': 'abc',
        #     'product_uom_qty': 1,
        #     'price_unit': 123,
        #     'order_id': self.id
        # })
        # print(data)


    # @api.model
    # def create(self, values):
    #     for order in self.filtered(lambda order: order.partner_id not in order.message_partner_ids):
    #         print(order.message_subscribe([order.partner_id.id]))
    #
    #     self.write({
    #         'state': 'sale',
    #         'confirmation_date': fields.Datetime.now()
    #     })
    #     return super(SaleOrder, self).create(values)
