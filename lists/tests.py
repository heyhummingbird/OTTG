from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item, List

class NewItemTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):
        correct_list = List.objects.create()
        other_list = List.objects.create()
  #      Item.objects.create(text='A new list item', list=correct_list)

        response = self.client.post(f'/lists/{correct_list.id}/add_item', 
            data = {'input_item': 'A new list item'})
 #       print(response)

        self.assertEqual(
            Item.objects.filter(list=correct_list).first().text, 
            'A new list item')

    def test_redirects_to_list_view(self):
        correct_list = List.objects.create()
        other_list = List.objects.create()

        response = self.client.post(f'/lists/{correct_list.id}/add_item', 
            data = {'input_item': 'A new list item'})

        self.assertRedirects(response, f'/lists/{correct_list.id}/')


class ListViewTest(TestCase):
    def test_displays_correct_list_items(self):
        correct_list = List.objects.create()
        Item.objects.create(text='item 1', list=correct_list)
        Item.objects.create(text='item 2', list=correct_list)

        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text='other list item 2', list=other_list)

        response = self.client.get(f'/lists/{correct_list.id}/')
        print(response)

        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(f'/lists/{list_.id}/')
        self.assertTemplateUsed(response, 'list.html')

class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        list_ = List()
        self.client.post('/lists/new', data = {
            'input_item': 'A new list item'})
#        print(repr(response.content.decode()))
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirect_after_POST(self):
        response = self.client.post('/lists/new', data = {'input_item': 'A new list item'})
#        print(response)
#        self.assertEqual(response.status_code, 302)
#        self.assertEqual(response['location'], '/lists/the-only-list/')
        list_ = List.objects.first()
        self.assertRedirects(response, f'/lists/{list_.id}/')

class ListAndItemModelsTest(TestCase):
    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        saved_list = List.objects.first()
#        self.assertEqual(saved_list.count(), 1)
        self.assertEqual(saved_list, list_)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.list, list_)

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
