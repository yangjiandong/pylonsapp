# -*- coding: utf-8 -*-

"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password

from routes import url_for
from webhelpers.html import literal,HTML
from pylons.controllers.util import abort, redirect_to

from webhelpers.html.tags import *

def format_environ(environ):
    result = []
    keys = environ.keys()
    keys.sort()
    for key in keys:
        result.append("%s: %r"%(key, environ[key]))
    return '\n'.join(result)

# 自定义
# 原样显示value
def emphasize(value):
    return literal('<em>') + value + literal('</em>')

# 全部处理value
def emphasize2(value):
    return literal('<em>' + value + '</em>')

def emphasize3(value):
    return HTML.em(value)

def emphasize4(value):
    return HTML.span(HTML.em(value))

def emphasize5(value):
    return HTML.span(HTML.em(value), id='first', class_='highlight')

