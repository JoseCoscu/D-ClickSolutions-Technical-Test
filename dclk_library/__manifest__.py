{
    'name': 'Library Management',
    'version': '18.0.1.0.0',
    'summary': 'Library book management with librarian role',
    'description': """
Library Management (Odoo 18)
===========================
- Manage library books
- Librarian security group
- Access control by role
    """,
    'author': 'JoseCoscu',
    'website': 'https://github.com/JoseCoscu',
    'category': 'Productivity',
    'depends': [
        'base',
    ],
    'data': [
        'security/library_groups.xml',
        'security/ir.model.access.csv',
        # 'views/library_book_views.xml',
        # 'views/library_menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
