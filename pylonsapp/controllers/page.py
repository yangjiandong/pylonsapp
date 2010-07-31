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

import formencode
from formencode import htmlfill
from pylons.decorators.rest import restrict
from pylons.decorators import validate

log = logging.getLogger(__name__)

class NewPageForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    content = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':'Please enter some content for the page.'
        }
    )
    heading = formencode.validators.String()
    title = formencode.validators.String(not_empty=True)

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

    def new(self):
        return render('/derived/page/new.html')

    @restrict('POST')
    @validate(schema=NewPageForm(), form='new')
    def create(self):
        page = Page()
        for k,v in self.form_result.items():
            setattr(page, k, v)
        meta.Session.add(page)
        meta.Session.commit()

        response.statsu_int = 302
        response.headers['location'] = h.url_for(controller='page', action='view', id=page.id)
        return "Moved temporarily"


    def edit(self, id=None):
        if id is None:
            abort(404)
        page_q = meta.Session.query(Page)
        page = page_q.filter_by(id=id).first()
        if page is None:
            abort(404)
        values = {
                  'title': page.title,
                  'heading': page.heading,
                  'content': page.content
                  }
        c.title = page.title
        return htmlfill.render(render('/derived/page/edit.html'), values)

    @restrict('POST')
    @validate(schema=NewPageForm(), form='edit')
    def save(self, id=None):
        page_q = meta.Session.query(Page)
        page = page_q.filter_by(id=id).first()
        if page is None:
            abort(404)
        for k,v in self.form_result.items():
            if getattr(page, k) != v:
                setattr(page, k, v)

        meta.Session.commit()
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='page', action='view',
                                                 id=page.id)
        return "Moved temporarily"

    def list(self):
        c.pages = meta.Session.query(Page)
        return render('/derived/page/list.html')

    def delete(self, id=None):
        if id is None:
            abort(404)

        page_q = meta.Session.query(Page)
        page = page_q.filter_by(id=id).first()

        if page is None:
            abort(404)

        meta.Session.delete(page)
        meta.Session.commit()
        return render('/derived/page/deleted.html')
