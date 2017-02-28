# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartnerIndustry(models.Model):
    _name = 'res.partner.industry'
    _decription = 'Partner Industry'

    name = fields.Char(
        required=True
    )
    description = fields.Text(
    )
