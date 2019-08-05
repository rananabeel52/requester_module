# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    service_ids = fields.One2many(comodel_name="customer.contract", inverse_name="res_partner_id", string="Service")


