# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from pylonsapp.lib.base import BaseController, render
import pylonsapp.lib.helpers as h

log = logging.getLogger(__name__)

class GreetingController(BaseController):

    def index(self):
        #http://pylonsbook.com/en/1.1/using-view-templates.html#security-considerations-and-webhelpers

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

    #采用cache
    def index_cache(self):
        c.greeting = h.literal('<b>Welcome</b>')
        c.name = 'Pylone 开发者!!，采用了cache,时间为 5 秒'
        return render('/greeting.html', cache_expire=5)

    def basic(self):
        return render('/basic.html')

    def context(self):
        return render('/context.html')

    def navigation(self):
        return render('/navigation.html')