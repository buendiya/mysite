import json
import os
import mysite.settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from shiyijian_pc_lib.LocalData.models import *
from django.core import serializers
serializer = serializers.get_serializer('json')()
results = []
results.extend(json.loads(serializer.serialize(RobotModel.objects.all())))

cur_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(cur_dir, 'fixture.json'), 'w') as f:
    f.write(json.dumps(results, indent=2))
