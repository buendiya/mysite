# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 20:05:45 2014

@author: jingsz
"""
import datetime
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView

def hello(request):
    return HttpResponse('{"delta":"this is delta", "desc":"this is desc"}', content_type="application/x-javascript")
    
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

class AboutView(TemplateView):
    template_name = "about.html"
