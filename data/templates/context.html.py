# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1280050104.8900001
_template_filename='D:\\workspace\\python\\workspace\\pylonsApp\\pylonsapp\\templates/context.html'
_template_uri='/context.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\r\n<body>\r\n')
        # SOURCE LINE 3

        context.write('<p>Here is an example:</p>')
        
        
        # SOURCE LINE 5
        __M_writer(u'\r\n<p>\r\n')
        # SOURCE LINE 7
        for key in context.keys():
            # SOURCE LINE 8
            __M_writer(u'The key is <tt>')
            __M_writer(escape(key))
            __M_writer(u'</tt>, the value is ')
            __M_writer(escape(str(context.get(key))))
            __M_writer(u'. <br />\r\n')
            pass
        # SOURCE LINE 10
        __M_writer(u'</p>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


