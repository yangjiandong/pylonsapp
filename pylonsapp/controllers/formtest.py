# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
#from pylons.controllers.util import abort, redirect_to
# 推荐采用h
import pylonsapp.lib.helpers as h

from pylonsapp.lib.base import BaseController, render
from paste.errordocument import custom_forward

log = logging.getLogger(__name__)

import formencode
from formencode import htmlfill

# 自定义验证
class CNDateConverter(formencode.validators.DateConverter):
    month_style = 'dd/mm/yyyy'

class EmailForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    email = formencode.validators.Email(not_empty=True)
    #date = formencode.validators.DateConverter(not_empty=True)
    date = CNDateConverter(not_empty=True)

class FormtestController(BaseController):

    def index(self):
        #c.email_msg = ''
        return render('/form/simpleform.html')

    def submit(self):
        #return 'Your email is : %s' % request.params['email']
        #h.redirect_to(controller='formtest', action='result')
        log.info('submit formtest')

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

    # 采用EmailForm
    # 验证信息自动为中文?
    def submit2(self):
        schema = EmailForm()
        try:
            c.form_result = schema.to_python(dict(request.params))
        except formencode.Invalid, error:
            c.form_result = error.value
            c.form_errors = error.error_dict or {}
            html = render('/form/simpleform.html')
            return htmlfill.render(
                                   html,
                                   defaults=c.form_result,
                                   errors=c.form_errors)

        else:
            return 'Your e-mail is: %s and the date selected was %r.' % (
                c.form_result['email'],
                c.form_result['date'],
            )


    def result(self):
        return 'Your data was successfully submitted.'

    from pylons.decorators import validate

    # 自定出错信息格式
    def custom_formatter(error):
        return '<span class="custom-message">%s</span><br />\n' % (
                htmlfill.html_quote(error)
        )

    # 采用标注方式
    @validate(schema=EmailForm(), form='index', post_only=False, on_get=True,
              auto_error_formatter=custom_formatter)
    def submit3(self):
        return 'Your email is: %s and the date selected was %r.' % (
                self.form_result['email'],
                self.form_result['date'],
                )

