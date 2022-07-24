import logging

#

from odoo import models, fields

_logger = logging.getLogger(__name__)


class OmkHospDoctor(models.Model):
    _name = "omk.hosp.doctor"
    _description = "Doctor"
    _inherit = "omk.hosp.person"

    specialization = fields.Char("Specialization", required=True)