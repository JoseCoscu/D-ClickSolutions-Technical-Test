from odoo import _, api, fields, models



class Library(models.Model):
    _name = 'library.library'

    name = fields.Char('Library Name', required=True)

