import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class OmkHospSampleType(models.Model):
    _name = "omk.hosp.sample_type"
    _description = "Analysis type"

    name = fields.Char("Sample's type", required=True, translate=True)
