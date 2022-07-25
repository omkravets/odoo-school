import logging

#

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class OmkHospDiagnosis(models.Model):
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

    diagnosis_date = fields.Date("Diagnosis date",
                                 required=True,
                                 default=fields.Date.today)

    treatment = fields.Text(string="Prescribed treatment")

    name = fields.Char(compute="_compute_diagnosis_name")

    intern = fields.Boolean(compute="_compute_intern")

    mentor = fields.Char(compute="_compute_mentor_name")

    mentors_comment = fields.Text("Mentor's comment")

    analysis_ids = fields.Many2many(comodel_name="omk.hosp.analysis",
                                    relation="diagnosis_to_analysis",
                                    column1="diagnosis_id",
                                    column2="analysis_id")

    @api.depends("patient_id", "doctor_id", "illness_id", "diagnosis_date")
    def _compute_diagnosis_name(self):
        # from datetime import date
        for diagn in self:
            patient_name = str(diagn.patient_id.name)
            diagnosis = str(diagn.illness_id.name)
            doctor_name = str(diagn.doctor_id.name)
            diagnosis_date = str(diagn.diagnosis_date)
            diagn.name = patient_name + " - " +\
                diagnosis + " (" +\
                doctor_name + ") - " + diagnosis_date

    @api.depends("doctor_id")
    def _compute_intern(self):
        for rec in self:
            if rec.doctor_id.intern:
                rec.intern = True
            else:
                rec.intern = False

    @api.depends("doctor_id")
    def _compute_mentor_name(self):
        for rec in self:
            if rec.doctor_id.mentor_id:
                rec.mentor = rec.doctor_id.mentor_id.name
            else:
                rec.mentor = ""
