import logging

from odoo import models, fields, api, exceptions, _

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

    doctor_id = fields.Many2one(string="Personal doctor",
                                comodel_name="omk.hosp.doctor",
                                ondelete="restrict")

    @api.depends("birth_date")
    def _compute_patient_age(self):

        from datetime import date

        today = date.today()
        for rec in self:
            if rec.birth_date:
                birthdate = rec.birth_date
                rec.age = today.year - birthdate.year - int((today.month, today.day) < (birthdate.month, birthdate.day))
            else:
                rec.age = ""

    @api.onchange("doctor_id")
    def _onchange_doctor_id(self):
        from datetime import date
        print("=============================================")
        # self.ensure_one()
        vals = {
                "patient_id": self.ids[0],
                "doctor_id": self.doctor_id.id,
                "date": date.today()
        }

        self.env['omk.hosp.assignment'].create(vals)
        return {
            "warning": {
                "title": "On change Personal Doctor",
                "message": "Змінили лікаря на " + self.doctor_id.name,
            }
        }
