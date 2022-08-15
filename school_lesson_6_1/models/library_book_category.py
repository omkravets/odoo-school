from odoo import api, fields, models


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Library Books Category'

    name = fields.Char('Title')

    book_ids = fields.One2many(
        string="Books in category",
        comodel_name="library.book",
        inverse_name="category_id"
    )
    active = fields.Boolean(
        string='Active',
        default=True,
    )
