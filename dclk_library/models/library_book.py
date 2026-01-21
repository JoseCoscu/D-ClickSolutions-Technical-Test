from odoo import _, api, fields, models



class LibraryBook(models.Model):
    _name = 'library.book'


    title = fields.Char('Book Title')
    author = fields.Char('Author')
    publish_date = fields.Date('Publish Date')
