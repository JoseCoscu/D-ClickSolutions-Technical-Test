from odoo import _, api, fields, models



class LibraryBook(models.Model):
    _name = 'library.book'


    name = fields.Char('Book Name', required=True, related='title', readonly=True)
    title = fields.Char('Book Title')
    author = fields.Char('Author')
    publish_date = fields.Date('Publish Date')
