# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name' : 'Website Sale Extension',
    'version': '10.0.1.0.0',
    'category': 'Website',
    'author': 'Rooms For (Hong Kong) Limited',
    'website': 'https://www.odoo-asia.com/',
    'summary': 'Website Sale Extension',
    'description': """
    
    Make company name required field.
    Reject "free" email addresses (@yahoo.co.jp, @gmail.com, etc.)
    
            """,
    'depends':[
        'website_sale',
    ],
    'data' : [
        ],
    'installable':True,
    'auto_install':False
}
