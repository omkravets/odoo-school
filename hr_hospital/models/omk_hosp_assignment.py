import logging


from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class OmkHospAssignment(models.Model):
    _name = "omk.hosp.assignment"
    _description = "Doctor assignment"

    patient_id = fields.Many2one(string="Patient",
                                 comodel_name="omk.hosp.patient",
                                 ondelete="restrict",
                                 required=True)

    doctor_id = fields.Many2one(string="Personal doctor",
                                comodel_name="omk.hosp.doctor",
                                ondelete="restrict",
                                required=True)

    date = fields.Date("Assignment date",
                       required=True,
                       default=fields.Date.today)

    name = fields.Char(compute="_compute_assignment_name")

    @api.depends("patient_id", "doctor_id", "date")
    def _compute_assignment_name(self):

        for assign in self:
            patient_name = str(assign.patient_id.name)
            doctor_name = str(assign.doctor_id.name)
            date = str(assign.date)

            assign.name = patient_name + " - " +\
                date + " (" +\
                doctor_name + ")"