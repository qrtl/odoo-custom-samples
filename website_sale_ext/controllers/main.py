# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.website_sale.controllers.main import WebsiteSale


FREE_DOMAIN = ['gmail.com', 'yahoo.co.jp']


class WebsiteSale(WebsiteSale):
    
    def _get_mandatory_billing_fields(self):
        required_fields = super(WebsiteSale, self).\
            _get_mandatory_billing_fields()
        required_fields.append('company_name')
        return required_fields

    def _get_mandatory_shipping_fields(self):
        required_fields = super(WebsiteSale, self).\
            _get_mandatory_shipping_fields()
        required_fields.append('company_name')
        return required_fields
    
    def checkout_form_validate(self, mode, all_form_values, data):
        error, error_message = super(WebsiteSale, self).checkout_form_validate(
            mode=mode, all_form_values=all_form_values, data=data)
        if data.get('email') and \
                        data.get('email').split("@",1)[1] in FREE_DOMAIN:
            error.update(email='Email can not be free domain address.')
            error_message.append('Please use your business email address.')
            return error, error_message
        return error, error_message
