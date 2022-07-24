import logging

#

from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class contact_person(models.Model):
    _name = "omk.hosp.contact_person"
    _description = "Contact persons"
    _inherit = "omk.hosp.person"
