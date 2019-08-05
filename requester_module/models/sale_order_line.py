# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    month = fields.Selection(string="Month", selection=[('january', 'January'), ('february	', 'February'),
                                                        ('march	', 'March'), ('april', 'April'),
                                                        ('may', 'May'), ('june', 'June'),
                                                        ('july	', 'July'), ('august', 'August'),
                                                        ('september', 'September'), ('october', 'October'),
                                                        ('november', 'November'), ('december', 'December')])
