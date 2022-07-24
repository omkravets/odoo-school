import logging

#

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class OmkHospPatient(models.Model):
    _name = "omk.hosp.patient"
    _description = "Patient"
    _inherit = "omk.hosp.person"

    birth_date = fields.Date("Birthdate", required=True)
    passport = fields.Char("Passport number")
    age = fields.Integer(compute="_compute_patient_age", compute_sudo=True)
    contact_person_id = fields.Many2one(string="Contact person",
                                        comodel_name="omk.hosp.contact_person",
                                        ondelete="restrict")

    @api.depends("birth_date")
    def _compute_patient_age(self):

        from datetime import date

        today = date.today()
        for patient in self:
            birthdate = patient.birth_date
            patient.age = today.year - birthdate.year - (
                (today.month, today.day) <
                (birthdate.month, birthdate.day))
