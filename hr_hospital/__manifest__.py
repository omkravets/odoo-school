{
    'name': "Hr_hospital",
    'summary': "",
    'author': "Oleksandr Kravets",

    'category': 'Productivity',
    'license': "LGPL-3",
    'version': "15.0.1.0.0",

    'depends': ['base'],


    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_main_menu.xml',
        'views/omk_hosp_patient_views.xml',
        'views/omk_hosp_doctor_views.xml',
        'views/omk_hosp_contact_person_views.xml',
        'views/omk_hosp_illness_views.xml',
        'views/omk_hosp_illness_type_views.xml',
        'views/omk_hosp_diagnosis_views.xml',
        'views/omk_hosp_visit_views.xml',
        'views/omk_hosp_assignment_views.xml',
        'views/omk_hosp_analysis_type_views.xml',
        'views/omk_hosp_sample_type_views.xml',
        'views/omk_hosp_analysis_views.xml',
        'wizard/omk_hosp_set_doctor_wizard_views.xml',
        'report/omk_hosp_report_templates.xml',
        'report/omk_hosp_report.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
    'price': 0,
    'currency': 'EUR',

}
