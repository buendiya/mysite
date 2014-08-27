from django.shortcuts import render_to_response, HttpResponse, RequestContext
from books.models import Book, Publisher
from django.http import HttpResponseRedirect
from books.forms import ContactForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from books.serializers import UserSerializer, GroupSerializer

import logging
logger = logging.getLogger('mysite.books')

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


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BookListView(ListView):
    model = Book

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'

class PublisherDetail(DetailView):
    model = Publisher
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context
    
    def get_object(self):
        super(PublisherDetail, self).get_object()
#         return get_object_or_404(User, pk=request.session['user_id'])







