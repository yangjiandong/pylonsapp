# -*- coding: utf-8 -*-

import logging

from pylons import request, response, session, tmpl_context as c
#from pylons.controllers.util import abort, redirect_to
# 推荐采用h
import pylonsapp.lib.helpers as h
import pylonsapp.model.meta as meta
#from pylonsapp.model import *
from pylonsapp.model import Page

from pylonsapp.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PageController(BaseController):

    def view(self, id=None):
#        c.title = 'Greetings'
#        c.heading = 'Sample Page'
#        c.content = 'This is page %s'%id

        if id is None:
            h.abort(404)

        page_q = meta.Session.query(Page)
        c.page = page_q.get(int(id))
        if c.page is None:
            h.abort(404)
        return render('/derived/page/view.html')

