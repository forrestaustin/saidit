# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1508152060.612204
_enable_loop = True
_template_filename = '/home/reddit/src/reddit/r2/r2/templates/privateinterstitial.html'
_template_uri = '/privateinterstitial.html'
_source_encoding = 'utf-8'
from r2.lib.filters import websafe, unsafe, conditional_websafe
from pylons import request
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import _, ungettext
_exports = ['interstitial_image_attrs', 'interstitial_message', 'interstitial_title', 'interstitial_buttons']


# SOURCE LINE 23

from r2.lib.template_helpers import static 


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'interstitial.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 50
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_image_attrs(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'\n  src="')
        # SOURCE LINE 30
        __M_writer(conditional_websafe(static('interstitial-image-private.png')))
        __M_writer(u'"\n  alt="')
        # SOURCE LINE 31
        __M_writer(conditional_websafe(_('private')))
        __M_writer(u'"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_message(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 38
        __M_writer(u'\n  <p>\n    ')
        # SOURCE LINE 40
        __M_writer(conditional_websafe(_("The moderators of this subreddit have set it to private. You must be a moderator or approved submitter to visit.")))
        __M_writer(u'\n  </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n  ')
        # SOURCE LINE 35
        __M_writer(conditional_websafe(_("You must be invited to visit this community")))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_interstitial_buttons(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        thing = context.get('thing', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n  <div class="buttons">\n    <a class="c-btn c-btn-primary login-required" href="/message/compose/?to=/r/')
        # SOURCE LINE 46
        __M_writer(conditional_websafe(thing.sr_name))
        __M_writer(u'">\n      ')
        # SOURCE LINE 47
        __M_writer(conditional_websafe(_("message the moderators")))
        __M_writer(u'\n    </a>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


