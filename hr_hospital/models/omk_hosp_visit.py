import logging

#

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class OmkHospVisit(models.Model):
    _name = "omk.hosp.visit"
    _description = "Visit"

    patient_id = fields.Many2one(string="Patient",
                                 comodel_name="omk.hosp.patient",
                                 ondelete="restrict",
                                 required=True)

    doctor_id = fields.Many2one(string="Doctor",
                                comodel_name="omk.hosp.doctor",
                                ondelete="restrict",
                                required=True)

    diagnosis_id = fields.Many2one(string="Diagnosis",
                                   comodel_name="omk.hosp.diagnosis",
                                   ondelete="restrict",
                                   required=True)

    visit_datetime = fields.Datetime("Visit date and time",
                                     required=True,
                                     default=fields.Date.today)

    recommendations = fields.Text(string="Visit recommendations")

    name = fields.Char(compute="_compute_visit_name")

    @api.depends("patient_id", "doctor_id", "visit_datetime")
    def _compute_visit_name(self):
        # from datetime import date
        for vis in self:
            patient_name = str(vis.patient_id.name)
            doctor_name = str(vis.doctor_id.name)
            date_time = str(vis.visit_datetime)

            vis.name = patient_name + " - " +\
                date_time + " (" +\
                doctor_name + ")"
