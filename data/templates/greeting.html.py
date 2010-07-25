# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1280051730.796
_template_filename='D:\\workspace\\python\\workspace\\pylonsApp\\pylonsapp\\templates/greeting.html'
_template_uri='/greeting.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


# SOURCE LINE 1

import datetime


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n\r\n<html>\r\n<head>\r\n    <title>Greetings2</title>\r\n</head>\r\n<body>\r\n    <h1>Greetings</h1>\r\n    ')
        # SOURCE LINE 11

    # c.greeting 处理为 h.literal('<b>Welcome</b>')
    

        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 13
        __M_writer(u'\r\n    <p>')
        # SOURCE LINE 14
        __M_writer(escape(c.greeting))
        __M_writer(u' Hello ')
        __M_writer(escape(c.name))
        __M_writer(u'!</p>\r\n    <p>')
        # SOURCE LINE 15
        __M_writer(escape(c.greeting))
        __M_writer(u' Hello ')
        __M_writer(escape(c.name3))
        __M_writer(u'!</p>\r\n    <p>')
        # SOURCE LINE 16
        __M_writer(escape(c.greeting))
        __M_writer(u' Hello ')
        __M_writer(escape(c.name4))
        __M_writer(u'!</p>\r\n    <p>')
        # SOURCE LINE 17
        __M_writer(escape(c.greeting))
        __M_writer(u' Hello ')
        __M_writer(escape(c.name5))
        __M_writer(u'!</p>\r\n\r\n<ul>\r\n')
        # SOURCE LINE 20
        for item in c.links:
            # SOURCE LINE 21
            __M_writer(u'    <li>')
            # SOURCE LINE 22
            if item[1]:
                # SOURCE LINE 23
                __M_writer(u'    <a href="')
                __M_writer(escape(item[1]))
                __M_writer(u'">')
                __M_writer(escape(item[0]))
                __M_writer(u'</a>')
                # SOURCE LINE 24
            else:
                # SOURCE LINE 25
                __M_writer(u'    ')
                __M_writer(escape(item[0]))
                __M_writer(u'')
                pass
            # SOURCE LINE 27
            __M_writer(u'    </li>\r\n')
            pass
        # SOURCE LINE 29
        __M_writer(u'</ul>\r\n\r\n')
        # SOURCE LINE 31

        title = 'Pylons Developer'
        names = [x[0] for x in c.links]
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['x','names','title'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 34
        __M_writer(u'\r\n')
        # SOURCE LINE 35
        for i, value in enumerate(names):
            # SOURCE LINE 36
            __M_writer(escape(i+1))
            __M_writer(u'. ')
            __M_writer(escape(value))
            __M_writer(u' <br />\r\n')
            pass
        # SOURCE LINE 38
        __M_writer(u'\r\nYour title is ')
        # SOURCE LINE 39
        __M_writer(escape(title))
        __M_writer(u'\r\n   ')
        # SOURCE LINE 40

         # This block can have any indentation as long as the Python
         #  code within it is properly indented
        if title == 'Pylons Developer':
            msg = 'You must program in Python!'
        else:
            msg = ''
             
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['msg'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 47
        __M_writer(u'\r\nAn optional message: ')
        # SOURCE LINE 48
        __M_writer(escape(msg))
        __M_writer(u'\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


