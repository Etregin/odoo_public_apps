# -*- coding: utf-8 -*-
{
    'name': 'Remove Powered by Odoo',
    'version': '1.0.0',
    'summary': """
        Remove Powered by Odoo from login page, portal sidebar, POS receipts, and brand promotion.
        Remove Manage Databases and database selector from login screen.
        Remove Odoo branding from portal pages, website footer and POS receipts.
        Hide Powered by Odoo. Remove Odoo branding. De-brand Odoo.
    """,
    'description': """
        Removing the 'Powered by' block entirely.
        Remove from the portal sidebar.
        Remove from the login page.
        Remove from POS receipt printouts.
        Remove from the brand promotion.
        Remove Odoo branding from the footer of portal pages.
        Remove Manage Databases link from login screen.
        Remove database selector from login screen.
        Hide Powered by Odoo.
    """,
    'author': 'Etregin',
    'company': 'Double Troubleshooting',
    "support": "etreginwow@gmail.com",
    'category': 'Tools',
    'sequence': 10,
    'depends': ['portal','point_of_sale'],
    'data': [
        'views/login_layout.xml',
        'views/portal_record_sidebar.xml',
        'views/brand_promotion.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'dt_remove_powered_by_odoo/static/src/app/screens/receipt_screen/receipt/order_receipt.xml',
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
    "price": 0.00,
    "currency": "USD",
}