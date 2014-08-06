from django.test import TestCase
import requests
# Create your tests here.

r = requests.get('http://127.0.0.1:8000/books/books/')
print r.status_code