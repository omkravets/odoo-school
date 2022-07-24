import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class OmkHospPerson(models.AbstractModel):
    _name = "omk.hosp.person"
    _description = "Person"

    name = fields.Char('Full name', required=True, translate=True)

    email = fields.Char(string="E-mail")

    phone_number = fields.Char(string="Phone")

    photo = fields.Image("Image", max_width=1024, max_height=1024)

    gender = fields.Selection([('male', 'male'), ('female', 'female')])
