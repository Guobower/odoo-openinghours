# -*- coding: utf-8 -*-
{
    'name': "Opening Hour",

    'summary': """
        This module is for configuring and create bussiness hour event on calendar""",

    'description': """
        This module is for configuring and create bussiness hour event on calendar
    """,

    'author': "Heru Prasetyo Utomo",
    'website': "https://hprasetyou.com",

    'category': 'calendar',
    'version': '0.1',
    'depends': ['base','calendar'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/cron.xml'
    ],
}
