# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Real Estate tutorial',
    'version': '0.1',
    'category': 'Sales/odoo-tutorial',
    'sequence': 15,
    'summary': 'Real Estate',
    'description': "",
    'website': 'https://www.odoo.com/page/odoo-tutorial',
    'depends': [
        'base',
        'web'
    ],
    'data': [        
        "security/ir.model.access.csv",
    ],
    'demo': [
        'data/crm_team_demo.xml',
        'data/mail_activity_demo.xml',
        'data/crm_lead_demo.xml',
    ],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False
}