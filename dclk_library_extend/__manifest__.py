{
    'name': 'Library Management Ext',
    'version': '18.0.1.0.0',
    'summary': 'Library book management with librarian role',
    'description': """
Library Management
===========================
- Manage library books
- Librarian security group
- Access control by role
    """,
    'author': 'JoseCoscu',
    'website': 'https://github.com/JoseCoscu',
    'category': 'Productivity',
    'depends': [
        'base','dclk_library', 'mail'
    ],
    'data': [
        'security/library_groups.xml',
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
