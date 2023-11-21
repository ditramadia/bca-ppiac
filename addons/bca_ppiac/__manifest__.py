# -*- coding: utf-8 -*-
{
    'name': "BCA PPIAC",
    'summary': 'Aplikasi Pusat Pertukaran Informasi Antar Cabang BCA.',
    'description': 'Sistem informasi untuk penyimpanan dan pertukaran informasi antar cabang BCA.',
    'sequence': -100,
    'author': "Pion-e4",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/data_menus.xml',
        'views/data_trees.xml',
        'views/data_forms.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
