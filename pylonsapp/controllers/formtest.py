# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
#from pylons.controllers.util import abort, redirect_to
# 推荐采用h
import pylonsapp.lib.helpers as h

from pylonsapp.lib.base import BaseController, render


log = logging.getLogger(__name__)

class FormtestController(BaseController):

    def index(self):
        return render('/form/simpleform.html')

    def submit(self):
        #return 'Your email is : %s' % request.params['email']
        #h.redirect_to(controller='formtest', action='result')

        # 增加验证
        c.email_msg = ''
        c.email_value = ''
        email = request.params.get('email')
        if not email:
            c.email_msg = "Please enter a value"
        elif '@' not in email:
            c.email_msg = "An email address must contain at least on '@' character."
        else:
            domain = email.split('@')[1]
            if '.' not in domain:
                c.email_msg = "An email address domain must contain "
                c.email_msg += "at least one '.' character."
            if not domain.split('.')[-1]:
                c.email_msg = "Please specify a domain type after the '.' character"

        if c.email_msg:
            c.email_value = email
            return render('/form/simpleform.html')

        return  'Your email is: %s' % request.params['email']



    def result(self):
        return 'Your data was successfully submitted.'
