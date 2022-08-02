import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class OmkHospPerson(models.AbstractModel):
    _name = "omk.hosp.person"
    _description = "Person"

    name = fields.Char(string='Full name', required=True, translate=True)

    email = fields.Char(string="E-mail")

    phone_number = fields.Char(string="Phone")

    photo = fields.Image(string="Image", max_width=1024, max_height=1024)

    gender = fields.Selection([('male', 'male'), ('female', 'female')])
