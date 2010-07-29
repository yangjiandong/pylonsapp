# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
#from pylons.controllers.util import abort, redirect_to
# 推荐采用h
import pylonsapp.lib.helpers as h

from pylonsapp.lib.base import BaseController, render

log = logging.getLogger(__name__)

from formencode.schema import Schema
from formencode.validators import Invalid, FancyValidator
from formencode.validators import Int, DateConverter, String, OneOf
from formencode import variabledecode
from formencode import htmlfill
from formencode.foreach import ForEach
from formencode.api import NoDefault

from formencode.validators import FancyValidator

class OneChiefInvestigator(FancyValidator):

    messages = {
        'too_many_cis':"Only one Chief Investigator is allowed, not %(number)s"
    }

    def validate_python(self, values, c):
       chief_investigators_found = 0
       for person in values['person']:
            if person['role'] == u'1':
                chief_investigators_found += 1
       if chief_investigators_found > 1:
            raise Invalid(
                self.message("too_many_cis", c, number=chief_investigators_found),
                values,
                c
            )

class Person(Schema):
    title = String()
    firstname = String(not_empty=True)
    surname = String(not_empty=True)
    role = OneOf(['1', '2', '3'])

class Study(Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    pre_validators = [variabledecode.NestedVariables()]
    title = String(not_empty=True)
    start_date = DateConverter()
    end_date = DateConverter()
    person = ForEach(
            Person(),
            if_missing=NoDefault,
            messages={'missing':'Please add a Person'}
            )

    chained_validators =[OneChiefInvestigator()]

def render_form(values=None, errors=None, number_of_people=0):
    c.number_of_people = number_of_people
    html = render('/derived/form.html')
    return htmlfill.render(html, defaults=values, errors=errors)

def number_of_people(values):
    people_count = 0
    for key in values.keys():
        if key.startswith('person-') and key.endswith('title'):
            people_count += 1
    return people_count

class StudyController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/study.mako')
        # or, return a response
        # return 'Hello World'
        return render_form()

    def process(self):
        action = request.params.getone('action')
        values = dict(request.params)
        # Don't use the values field for repopulation
        del values['action']
        if action == 'Add New Person':
            # Render the form with one extra set of person fields
            return render_form(
                values=values,
                number_of_people = number_of_people(values) + 1
            )
        elif action.startswith('Remove'):
            # Get the ID of the set of person fields to remove
            id = int(action.split(' ')[-1])
            # Create a new set of values without those fields
            new_values = {}
            for k, v in values.items():
                if k.startswith('person-'):
                    name, field = k.split('.')
                    cur_id = int(name[len('person')+1:])
                    if cur_id<id:
                        new_values[k] = v
                    elif cur_id>id:
                        new_values['person-%s.%s'%(cur_id-1, field)] = v
                else:
                    new_values[k] = v
            # Render the form with the new values
            return render_form(
                values=new_values,
                number_of_people = number_of_people(new_values)
            )
        elif action=='Save':
            # Assume we are trying to save the form
            schema = Study()
            try:
                result = schema.to_python(dict(request.params), c)
            except Invalid, e:
                return render_form(
                    values=values,
                    errors=variabledecode.variable_encode(
                        e.unpack_errors() or {},
                        add_repetitions=False
                    ),
                    number_of_people=number_of_people(values)
                )
            else:
                # You would save the data here before redirecting
                # values will be a Python nested data structure
                # which shouldn't need any further conversion.

                # In this case we just display the result
                return str(result)
        else:
            raise Exception('Invalid action %s'%action)

