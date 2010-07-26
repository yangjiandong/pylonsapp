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
        h.redirect_to(controller='formtest', action='result')

    def result(self):
        return 'Your data was successfully submitted.'
