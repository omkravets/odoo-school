import logging

from odoo import _, api, models, fields

_logger = logging.getLogger(__name__)


class OmkHospChangeDoctorWizard(models.TransientModel):

    _name = "omk.hosp.set_doctor_wizard"
    _description = "Multi change personal doctor"

    doctor_id = fields.Many2one(string="Doctor",
                                comodel_name="omk.hosp.doctor",
                                required=True)

    def set_doctor(self):
        # logging.info("+++++++++++++++++++++++++++++++++++++++++++++++")
        # logging.info(f"-----------------{self.doctor_id.name}----------------")
        patients = self.env['omk.hosp.patient'].browse(self._context.get('active_ids'))
        for patient in patients:
            logging.info(f"{patient.name} ---- {patient.doctor_id.name}")
            patient.doctor_id = self.doctor_id
