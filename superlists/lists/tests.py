from django.http import HttpRequest
from django.test import TestCase

print("Hello ------------------------- here")
# Create your tests here
from .views import home_page



class HomePageViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('<title>To-Do</title>', response.content.decode('utf8'))
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertTrue(response.content.endswith(b'</html>'))
