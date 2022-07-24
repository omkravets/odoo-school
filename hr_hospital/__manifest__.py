# -*- coding: utf-8 -*-
{
    'name': "Hr_hospital",
    'summary': "",
    'author': "omkravets",

    'category': 'Productivity',
    'license': "LGPL-3",
    'version': "15.0.1.0.0",

    'depends': ['base'],


    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/contact_person.xml',
        'views/illness.xml',
        'views/diagnosis.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
    'price': 0,
    'currency': 'EUR',

}

