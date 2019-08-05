# -*- coding: utf-8 -*-
{
    'name': "Customer Request",
    'summary': """
        This is Customer Request Module""",
    'description': """
        This is Customer Request Module
    """,
    'author': "SolutionFounder",
    'website': "http://www.solutionfounder.com",
    'category': 'sale',
    'version': '12.0.0.1',
    'depends': ['base', 'mail', 'web', 'account','sale_management'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/requester_data.xml',
        'views/requester_module.xml',
        'views/sequence.xml',
        'web_template/requester_form_view.xml',
        'data/mail_template.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/menues.xml',
    ],
}
