from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page


# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(3, 3)

class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
#        request = HttpRequest()
#        found = resolve('/')
#        response = found.func(request)
        response = self.client.get('/')
#        html = response.content.decode('utf8')
#        print(repr(html))
#        self.assertTrue(html.startswith('<html>'))
#        self.assertIn('<title>To-Do Lists</title>', html)
#        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data = {'input_item': 'A new list item'})
#        print(repr(response.content.decode()))
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

# Create your tests here.
