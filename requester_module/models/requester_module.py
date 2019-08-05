# -*- coding: utf-8 -*-
from odoo import models, fields, api


class RequesterModule(models.Model):
    _name = 'requester.module'
    _inherit = ['mail.thread']
    _description ="Requester"

    name = fields.Char('My Sequence')
    state = fields.Selection(string="State", selection=[('draft', 'Draft'), ('send_request', 'Send Request'),
                                                        ('confirm_request', 'Confirm Request')], default='draft',
                                    track_visibility='always', track_sequence=4)
    price = fields.Float(string="Price", track_visibility='always', track_sequence=2)
    discount = fields.Float(string="Discount", track_visibility='always', track_sequence=3)
    req_name = fields.Char(string="Requester Name", track_visibility='always', track_sequence=1)
    phone = fields.Char(string="Phone Number")
    email = fields.Char(string="Email")
    range = fields.Integer(string="Range")
    person = fields.Integer(string="Person")

    @api.multi
    def _track_subtype(self, init_values):
        self.ensure_one()
        if 'state' in init_values and self.state == 'draft':
            return 'requester_module.mt_requestm_created'
        return super(RequesterModule, self)._track_subtype(init_values)

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('code')
        return super(RequesterModule, self.with_context(mail_create_nolog=True)).create(vals)

    @api.multi
    def send(self):
        self.state = 'send_request'

    @api.one
    def confirm_request(self):
        self.state = 'confirm_request'
        templ_id = self.env.ref('requester_module.example_email_template')
        self.env['mail.template'].browse(templ_id.id).send_mail(self.id)

    @api.multi
    def create_customer(self):
        print("ABC")


