import logging

#

from odoo import models, fields

_logger = logging.getLogger(__name__)


class OmkHospDoctor(models.Model):
    _name = "omk.hosp.doctor"
    _description = "Doctor"
    _inherit = "omk.hosp.person"

    specialization = fields.Char(required=True)
    is_intern = fields.Boolean(string="Intern",
                               default=False)
    mentor_id = fields.Many2one(string="Mentor",
                                comodel_name="omk.hosp.doctor",
                                ondelete="restrict")
    intern_ids = fields.One2many(string="Interns",
                                 comodel_name="omk.hosp.doctor",
                                 inverse_name="mentor_id")
    patient_ids = fields.One2many(string="personal patients",
                                  comodel_name="omk.hosp.patient",
                                  inverse_name="doctor_id")

    def omk_hosp_add_visit_from_doctor_view(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Visit",
            "res_model": "omk.hosp.visit",
            "view_type": "form",
            "view_mode": "form",
            #  "context": {"default_patient_id": self.ids[0]},
            'view_id': self.env.ref("hr_hospital.omk_hosp_visit_form").id,
            "target": "new",
        }
