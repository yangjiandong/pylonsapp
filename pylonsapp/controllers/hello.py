# -*- coding: utf-8 -*-

import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from pylonsapp.lib.base import BaseController, render
import pylonsapp.lib.helpers as h
from pylons import app_globals
from pylons import config

log = logging.getLogger(__name__)

class HelloController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/hello.mako')
        # or, return a response

        # the browser treats the message as plain text instead of HTML
        response.content_type = 'text/plain'
        return 'Hello World,再加中文!'

    def environ(self):
        result='<html><body><h1>Environ</h1>'
        for key, value in request.environ.items():
            result +='%s:%r <br/>'%(key, value)
        result += '</body></html>'
        return result

    # use helper
    def environ2(self):
        response.content_type='text/plain'
        return h.format_environ(request.environ)

    def test_abort(self):
        username = request.environ.get('REMOTE_USER')
        if not username:
            abort(401)
        else:
            return "Hello %s" %username

    # 公共变量
    def app_globals_test(self):
        app_globals.visits +=1
        return "You are visitor numer %s." %app_globals.visits

    def debugger(self):
        value = "some value"
        raise Exception("Just testing the interactive debugger!")
