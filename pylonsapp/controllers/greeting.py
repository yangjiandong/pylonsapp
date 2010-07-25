# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from pylonsapp.lib.base import BaseController, render

log = logging.getLogger(__name__)

class GreetingController(BaseController):

    def index(self):
        #http://pylonsbook.com/en/1.1/using-view-templates.html#security-considerations-and-webhelpers
        import pylonsapp.lib.helpers as h
        c.greeting = h.literal('<b>欢迎!</b>')
        # 采用自定义
        c.name = h.emphasize2('Pylons <b>Developer</b>,use c')
        c.name3 = h.emphasize3('Pylons <b>Developer</b>,use c')
        c.name4 = h.emphasize4('Pylons <b>Developer</b>,use c')
        c.name5 = h.emphasize5('Pylons Developer,use c')
        c.links = [
                   ('James', 'http://jimmyg.org'),
                   ('Ben', 'http://groovie.org'),
                   ('Philip', ''),
                   ]

        #return render('/greeting.html', extra_vars={'name':name})
        return render('/greeting.html')

    def context(self):
        return render('/context.html')