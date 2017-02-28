# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_no = fields.Char(
        string="Partner Number",
        readonly=False,
        copy=False,
    )
    industry_id = fields.Many2one(
        comodel_name='res.partner.industry',
        required=True,
    )
    contract_type = fields.Selection(
        [('monthly', 'Monthly'),
         ('yearly', 'Yearly')],
        string='Contract Type',
    )
    bank_account = fields.Char(
        'Bank Account',
    )

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(partner_no)',
         "Partner number must be unique."),
    ]

    @api.model
    def create(self, vals):
        if vals['is_company'] or (not vals['is_company']
                                  and not vals['parent_id']):
            partner_no = self.env['ir.sequence'].next_by_code('res.partner')
            vals.update({'partner_no': partner_no})
        return super(ResPartner, self).create(vals)

