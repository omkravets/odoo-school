import logging

#

from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class doctor(models.Model):
    _name = "omk.hosp.doctor"
    _description = "Doctor"
    _inherit = "omk.hosp.person"

    specialization = fields.Char("Specialization", required=True)