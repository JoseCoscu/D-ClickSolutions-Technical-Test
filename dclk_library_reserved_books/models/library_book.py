from odoo import _, api, fields, models
from odoo.exceptions import UserError


class LibraryBook(models.Model):
    _inherit = 'library.book'

    state = fields.Selection([('available', 'Available'), ('borrowed', 'Borrowed'), ('reserved', 'Reserved')],
                             default='available', tracking=True)
    is_reserved = fields.Boolean(string='Reserved')
    reserved_to = fields.Many2one('res.users', string='Reserved To', readonly=True, tracking=True)
    reserved_date = fields.Date(string='Reserved Date', readonly=True, tracking=True)
    reserved_end_date = fields.Date(string='Reserved ends on', readonly=True, tracking=True)

    def reserve_book(self):
        if self.is_borrowed:
            raise UserError(_('You cannot reserve a borrowed book'))
        return {
            'type': 'ir.actions.act_window',
            'name': 'Reserve Book',
            'res_model': 'book.reservations',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_user_id': self.env.user.id,
                'default_book_id': self.id,
            }
        }

    def borrow_book(self):
        if self.is_reserved:
            raise UserError('Cannot borrow reserved book')
        super().borrow_book()
        self.state = 'borrowed'

    def return_book(self):
        super().return_book()
        self.state = 'available'
        self.is_reserved = False
        self.reserved_to = None
        self.reserved_date = None
        self.reserved_end_date = None
