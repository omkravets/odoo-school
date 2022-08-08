import logging
from datetime import date

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

    assignment_ids = fields.One2many(string="Assignment",
                                     comodel_name="omk.hosp.assignment",
                                     inverse_name="patient_id")

    diagnosis_ids = fields.One2many(string="Diagnoses",
                                    comodel_name="omk.hosp.diagnosis",
                                    inverse_name="patient_id")

    doctor_id = fields.Many2one(string="Personal doctor",
                                comodel_name="omk.hosp.doctor",
                                ondelete="restrict")

    @api.depends("birth_date")
    def _compute_patient_age(self):

        today = date.today()
        for rec in self:
            if rec.birth_date:
                birthdate = rec.birth_date
                rec.age = today.year - birthdate.year - \
                    int((today.month, today.day) <
                        (birthdate.month, birthdate.day))
            else:
                rec.age = ""

    @api.model
    def create(self, vals):
        # при створенні нового пацієнта
        new_record = super().create(vals)
        if "doctor_id" in vals:
            self.env['omk.hosp.assignment'].create({
                "doctor_id": vals["doctor_id"],
                "patient_id": new_record.id,
                "date": date.today()
            })
        return new_record

    def write(self, vals):
        # при оновленні даних пацієнта
        if "doctor_id" not in vals:
            # якщо ми не задали лікаря
            return super().write(vals)

        for rec in self:
            if rec.doctor_id != vals.get("doctor_id"):
                # якщо лікар, якого задали змінився
                self.env['omk.hosp.assignment'].create({
                    "doctor_id": vals["doctor_id"],
                    "patient_id": rec.id,
                    "date": date.today()
                })
        return super().write(vals)

    def omk_hosp_visit_act_window(self):
        return{
            "type": "ir.actions.act_window",
            "name": "Visits",
            "res_model": "omk.hosp.visit",
            "view_type": "form",
            "view_mode": "tree,form",
            "domain": [("patient_id", "=", self.id)],
            "target": "current",
        }

    def omk_hosp_assignment_act_window(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Assignments",
            "res_model": "omk.hosp.assignment",
            "view_type": "form",
            "view_mode": "tree,form",
            "domain": [("patient_id", "=", self.id)],
            "target": "current",
        }

    def omk_hosp_analysis_act_window(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Analyses",
            "res_model": "omk.hosp.analysis",
            "view_type": "form",
            "view_mode": "tree,form",
            "domain": [("patient_id", "=", self.id)],
            "target": "current",
        }
