import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class OmkHospIllnessType(models.Model):
    _name = "omk.hosp.illness_type"
    _description = "Illness"

    name = fields.Char('Illness type', required=True, translate=True)
    full_name = fields.Char(string="Full name", compute="_compute_full_name", recursive=True, store=True)
    parent_id = fields.Many2one(comodel_name="omk.hosp.illness_type", string="Parent")
    child_ids = fields.One2many(comodel_name='omk.hosp.illness_type', inverse_name='parent_id', string='Sub Levels')

    @api.depends("name", "parent_id.full_name")
    def _compute_full_name(self):
        for rec in self:
            if rec.parent_id:
                rec.full_name = f"{rec.parent_id.full_name} / {rec.name}"
            else:
                rec.full_name = rec.name
