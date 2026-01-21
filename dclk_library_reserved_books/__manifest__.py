{
    'name': 'Library Management Reserved Books',
    'version': '18.0.1.0.0',
    'summary': 'Library book management reserved',
    'description': """
Library Management
===========================
- Manage library books state
- Manage books reserves
    """,
    'author': 'JoseCoscu',
    'website': 'https://github.com/JoseCoscu',
    'category': 'Productivity',
    'depends': [
        'base','dclk_library', 'dclk_library_extend'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_library.xml',
        'data/library_library_data.xml',
        'wizards/library_reservations_views.xml'
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
