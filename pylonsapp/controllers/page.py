# -*- coding: utf-8 -*-

import logging

from pylons import request, response, session, tmpl_context as c
#from pylons.controllers.util import abort, redirect_to
# 推荐采用h
import pylonsapp.lib.helpers as h

from pylonsapp.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PageController(BaseController):

    def view(self, id):
        c.title = 'Greetings'
        c.heading = 'Sample Page'
        c.content = 'This is page %s'%id
        return render('/derived/page/view.html')

