# -*- coding: utf-8 -*-
# Copyright 2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Add Fields to Partner",
    "summary": "",
    "version": "10.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://www.odoo-asia.com/",
    "author": "Rooms For (Hong Kong) Limited T/A OSCG",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "pre_init_hook": "",
    "post_init_hook": "",
    "post_load": "",
    "uninstall_hook": "",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "sale",
    ],
    "data": [
        'security/ir.model.access.csv',
        'data/res_partner_data.xml',
        'views/res_partner_industry_views.xml',
        'views/res_partner_views.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
