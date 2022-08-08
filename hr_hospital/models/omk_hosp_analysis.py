import logging


from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class OmkHospAnalysis(models.Model):
    _name = "omk.hosp.analysis"
    _description = "Analysis"

    patient_id = fields.Many2one(string="Patient",
                                 comodel_name="omk.hosp.patient",
                                 ondelete="restrict",
                                 required=True)

    doctor_id = fields.Many2one(string="Doctor",
                                comodel_name="omk.hosp.doctor",
                                ondelete="restrict",
                                required=True)

    date = fields.Date(string="Date of analysis",
                       required=True,
                       default=fields.Date.today)

    analysis_type_id = fields.Many2one(string="Analysis type",
                                       comodel_name="omk.hosp.analysis_type",
                                       ondelete="restrict",
                                       required=True)

    sample_type_id = fields.Many2one(string="Sample's Type",
                                     comodel_name="omk.hosp.sample_type",
                                     ondelete="restrict",
                                     required=True)

    conclusion = fields.Text(string="Conclutions",
                             required=True)

    diagnosis_ids = fields.Many2many(comodel_name="omk.hosp.diagnosis",
                                     relation="diagnosis_to_analysis",
                                     column2="diagnosis_id",
                                     column1="analysis_id")

    name = fields.Char(compute="_compute_analysis_name")

    @api.depends("patient_id", "analysis_type_id")
    def _compute_analysis_name(self):
        for rec in self:
            rec.name = f"{self.patient_id.name} -- " \
                       f"{self.analysis_type_id.name}"
