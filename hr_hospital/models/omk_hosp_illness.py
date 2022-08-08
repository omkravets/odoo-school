import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class OmkHospIllness(models.Model):
    _name = "omk.hosp.illness"
    _description = "Illness"

    name = fields.Char('Illness name',
                       required=True,
                       translate=True)
    illness_type_id = fields.Many2one(string="Illness type",
                                      comodel_name="omk.hosp.illness_type",
                                      ondelete="cascade",
                                      required=True)
    type_full_name = fields.Char(string="Type Full name",
                                 compute="_compute_type_full_name",
                                 store=True)

    @api.depends("illness_type_id")
    def _compute_type_full_name(self):
        for rec in self:
            rec.type_full_name = rec.illness_type_id.full_name
