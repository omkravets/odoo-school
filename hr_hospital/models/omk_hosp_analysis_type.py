import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class OmkHospAnalysisType(models.Model):
    _name = "omk.hosp.analysis_type"
    _description = "Analysis type"

    name = fields.Char(string='Analysis type', required=True, translate=True)
    parent_id = fields.Many2one("omk.hosp.analysis_type", string="Parent")
    child_ids = fields.One2many('omk.hosp.analysis_type',
                                'parent_id', string='Sub Levels')
