import logging

#

from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class patient(models.Model):
    _name = "omk.hosp.diagnosis"
    _description = "Diagnosis"

    patient_id = fields.Many2one(string="Patient",
                                 comodel_name="omk.hosp.patient",
                                 ondelete="restrict",
                                 required=True)

    doctor_id = fields.Many2one(string="Doctor",
                                comodel_name="omk.hosp.doctor",
                                ondelete="restrict",
                                required=True)

    illness_id = fields.Many2one(string="Illness",
                                 comodel_name="omk.hosp.illness",
                                 ondelete="restrict",
                                 required=True)

    diagnosis_date = fields.Date("Diagnosis", required=True, default=fields.Date.today)

    treatment = fields.Text(string="Prescribed treatment")

    name = fields.Char(compute="_compute_diagnosis_name")

    @api.depends("patient_id", "doctor_id", "illness_id", "diagnosis_date")
    def _compute_diagnosis_name(self):
        # from datetime import date
        for diagn in self:
            patient_name = str(diagn.patient_id.name)
            diagnosis = str(diagn.illness_id.name)
            doctor_name = str(diagn.doctor_id.name)
            diagn.name = patient_name + " - " + diagnosis + " (" + doctor_name + ")"
