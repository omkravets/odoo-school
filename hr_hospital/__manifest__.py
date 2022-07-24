# -*- coding: utf-8 -*-
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
        'views/omk_hosp_patient.xml',
        'views/omk_hosp_doctor.xml',
        'views/omk_hosp_contact_person.xml',
        'views/omk_hosp_illness.xml',
        'views/omk_hosp_diagnosis.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
    'price': 0,
    'currency': 'EUR',

}

