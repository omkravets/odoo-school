import logging

#

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class OmkHospDoctor(models.Model):
    _name = "omk.hosp.doctor"
    _description = "Doctor"
    _inherit = "omk.hosp.person"

    specialization = fields.Char(required=True)
    intern = fields.Boolean(default=False)
    mentor_id = fields.Many2one(string="Mentor",
                                comodel_name="omk.hosp.doctor",
                                ondelete="restrict")
    intern_ids = fields.One2many(string="Interns",
                                 comodel_name="omk.hosp.doctor",
                                 inverse_name="mentor_id")
