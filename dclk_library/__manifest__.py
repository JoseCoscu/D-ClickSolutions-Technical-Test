{
    'name': 'Library Management',
    'version': '18.0.1.0.0',
    'summary': 'Library book management',
    'description': """
Library Management
===========================
- Manage library books
    """,
    'author': 'JoseCoscu',
    'website': 'https://github.com/JoseCoscu',
    'category': 'Productivity',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'data/library_book_demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
