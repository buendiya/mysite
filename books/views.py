from django.shortcuts import render_to_response, HttpResponse, RequestContext
from books.models import Book
        
from django.http import HttpResponseRedirect

from books.forms import ContactForm

import logging
logger = logging.getLogger('mysite.books')

## Create your views here.
#def search_form(request):
#    return render(request, 'search_form.html')
#
#def search(request):
#    q = request.GET['q']
#    if q:
#        books = Book.objects.filter(title__icontains=q)
#        return render_to_response('search_results.html',
#            {'books': books, 'query': q})
#    else:
#        return render_to_response('search_form.html', {'error': True})

#def search(request):
#    error = False
#    if 'q' in request.GET:
#        q = request.GET['q']
#        if not q:
#            error = True
#        elif len(q) > 20:
#            error = True
#        else:
#            books = Book.objects.filter(title__icontains=q)
#            return render_to_response('search_results.html',
#                {'books': books, 'query': q})
#    return render_to_response('search_form.html',
#        {'error': error})

def search(request):
    logger.info("request.method: %s", request.method)
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors })


def contact(request):
    logger.info("request.method: %s", request.method)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
#            send_mail(
#                cd['subject'],
#                cd['message'],
#                cd.get('email', 'noreply@example.com'),
#                ['siteowner@example.com'],
#            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render_to_response('contact_form.html', {'form': form}, context_instance=RequestContext(request))


def thanks(request):
    logger.info("request.method: %s", request.method)
    return render_to_response('thanks.html', context_instance=RequestContext(request))

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

