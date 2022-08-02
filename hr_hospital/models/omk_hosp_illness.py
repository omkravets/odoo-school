import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class OmkHospIllness(models.Model):
    _name = "omk.hosp.illness"
    _description = "Illness"

    name = fields.Char('Illness name', required=True, translate=True)
    parent_id = fields.Many2one(comodel_name="omk.hosp.illness", string="Parent")
    child_ids = fields.One2many(comodel_name='omk.hosp.illness', inverse_name='parent_id', string='Sub Levels')
