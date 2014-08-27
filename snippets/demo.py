import os
import sys
import datetime
cur_dir = os.path.dirname(__file__)
sys.path.append(os.path.dirname(cur_dir))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print "hello, world"\n')
snippet.save()

serializer = SnippetSerializer(snippet)
print serializer.object
serializer.data

content = JSONRenderer().render(serializer.data)
content

from rest_framework.compat import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)

serializer = SnippetSerializer(data=data)
print serializer.data
serializer.is_valid()
# True
print serializer.object

serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data


class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')

from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def restore_object(self, attrs, instance=None):
        """
        Given a dictionary of deserialized field values, either update
        an existing model instance, or create a new model instance.
        """
        if instance is not None:
            instance.email = attrs.get('email', instance.email)
            instance.content = attrs.get('content', instance.content)
            instance.created = attrs.get('created', instance.created)
            return instance
        return Comment(**attrs)

serializer = CommentSerializer(comment)
print serializer.data
from rest_framework.renderers import JSONRenderer

json = JSONRenderer().render(serializer.data)
print json

from StringIO import StringIO
from rest_framework.parsers import JSONParser

stream = StringIO(json)
data = JSONParser().parse(stream)

serializer = CommentSerializer(data={'email': 'foobar', 'content': 'baz'})
serializer.is_valid()


