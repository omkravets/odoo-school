import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class OmkHospSampleType(models.Model):
    _name = "omk.hosp.sample_type"
    _description = "Sample's type"

    name = fields.Char("Sample's type", required=True, translate=True)
    parent_id = fields.Many2one(string="Parent",
                                comodel_name="omk.hosp.sample_type")
    child_ids = fields.One2many(string="Sub category",
                                comodel_name="omk.hosp.sample_type",
                                inverse_name="parent_id")
    full_name = fields.Char(string="Full path",
                            compute="_compute_full_name",
                            recursive=True,
                            store=True)

    @api.depends("name", "parent_id.full_name")
    def _compute_full_name(self):
        for rec in self:
            if rec.parent_id:
                rec.full_name = f"{rec.parent_id.full_name} / {rec.name}"
            else:
                rec.full_name = rec.name
