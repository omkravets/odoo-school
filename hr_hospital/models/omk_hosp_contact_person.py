import logging

#

from odoo import models

_logger = logging.getLogger(__name__)


class OmkHospContactPerson(models.Model):
    _name = "omk.hosp.contact_person"
    _description = "Contact persons"
    _inherit = "omk.hosp.person"
