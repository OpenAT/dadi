# -*- coding: utf-8 -*-
#from openerp.addons.website_crm.controllers import main

from openerp import http
from openerp.addons.website_crm.controllers.main import contactus


class contactus_dadi(contactus):
    # Remove "company name" from the required fields in the contact form
    @http.route()
    def contactus(self, **kwargs):
        # original Value: ['name', 'contact_name', 'email_from', 'description']
        # "name" refers to the company name so we remove it from the required fields
        self._REQUIRED = ['contact_name', 'email_from', 'description']
        return super(contactus_dadi, self).contactus(**kwargs)
