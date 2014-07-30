import os
import sys
cur_dir = os.path.dirname(__file__)
sys.path.append(os.path.dirname(cur_dir))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from restSnippets.models import Snippet
from restSnippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print "hello, world"\n')
snippet.save()

serializer = SnippetSerializer(snippet)
print serializer.data
print 'serializer.data: ', type(serializer.data)

content = JSONRenderer().render(serializer.data)
print content
print 'content: ', type(content)

# This import will use either `StringIO.StringIO` or `io.BytesIO`
# as appropriate, depending on if we're running Python 2 or Python 3.
from rest_framework.compat import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)
print data
print 'data:', type(data)

serializer = SnippetSerializer(data=data)
print serializer.data
print 'serializer.data: ', type(serializer.data)
print serializer.is_valid()
# True
print serializer.object
# <Snippet: Snippet object>




