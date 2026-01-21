from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class BookReservations(models.TransientModel):
    _name = 'book.reservations'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    user_id = fields.Many2one('res.users', string='User', required=True)
    reservation_date = fields.Date(string='Reservation Date', required=True, default=fields.Date.today)
    reservation_end_date = fields.Date(string='Reservation End', required=True)
    library_id = fields.Many2one('library.library', string='Library', required=True)

    @api.constrains('reservation_date', 'reservation_end_date')
    def _check_reservation_dates(self):
        today = fields.Date.today()
        for record in self:
            if record.reservation_date < today:
                raise ValidationError(
                    _("The reservation start date cannot be earlier than today.")
                )

            if record.reservation_end_date < record.reservation_date:
                raise ValidationError(
                    _("The reservation end date cannot be earlier than the reservation start date.")
                )

    def action_reserve_book(self):
        self.book_id.state = 'reserved'
        self.book_id.is_reserved = True
        self.book_id.reserved_to = self.user_id
        self.book_id.reserved_date = self.reservation_date
        self.book_id.reserved_end_date = self.reservation_end_date
        return
