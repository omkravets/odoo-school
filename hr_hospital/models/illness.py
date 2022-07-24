import logging

from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class illness(models.Model):
    _name = "omk.hosp.illness"
    _description = "Illness"

    name = fields.Char('Illness name', required=True, translate=True)
    parent_id = fields.Many2one("omk.hosp.illness", string="Parent")



