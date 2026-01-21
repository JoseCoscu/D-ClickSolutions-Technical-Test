from odoo import fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _inherit = ['library.book','mail.thread', 'mail.activity.mixin']

    is_borrowed = fields.Boolean('Is borrowed', readonly=True, tracking=True)

    # state = fields.Selection([('available', 'Available'), ('borrowed', 'Borrowed'), ('reserved', 'Reserved')],
    #                          default='available')

    def borrow_book(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False
