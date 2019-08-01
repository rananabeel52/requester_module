# -*- coding: utf-8 -*-
{
    'name': "Requester Module",
    'summary': """
        This is Requester Rule Module""",
    'description': """
        This is Requester Rule Module
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/requester_data.xml',
        'views/requester_module.xml',
        'views/sequence.xml',
        'web_template/requester_form_view.xml',
        'data/mail_template.xml',
        # 'views/templates.xml',
    ],
}
