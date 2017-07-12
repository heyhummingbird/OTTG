from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest

MAX_WAIT = 5

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                ## <tr> </tr> specifies a row
                ## rows is a "list"
                self.assertIn(
                    row_text,
                    [row.text for row in rows], 
                    f"New to-do item didn't appear in the table. Contents were:\n{table.text}"
                )
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.1)


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        print(self.live_server_url)
        self.browser.get(self.live_server_url)
        ## 不在 8000 上面測試

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.assertIn('To-Do', self.browser.find_element_by_tag_name('h1').text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            'Enter a to-do item', 
            inputbox.get_attribute('placeholder')
        )
        
        # She types "Read OS" into a text box
        inputbox.send_keys('Read OS')
        
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Read OS')
        
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        ## We have to redefine inputbox after the page updates
        inputbox.send_keys('Write songs')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        
        self.wait_for_row_in_list_table('1: Read OS')
        self.wait_for_row_in_list_table('2: Write songs')


        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        
        # She visits that URL - her to-do list is still there.
        
        # Satisfied, she goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        print(self.live_server_url)
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Read OS')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Read OS')

        edith_url = self.browser.current_url
        self.assertRegex(edith_url, '/lists/.+')
        ## '.' for any character, '+' for 1 or more repititions

        # Now a new user, Francis, comes along to the site.

        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc

        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page. There is no sign of Edith's list
        self.browser.get(self.live_server_url)
        page_content = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Read OS', page_content)
        self.assertNotIn('Write songs', page_content)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Communicate with Testing Goat')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Communicate with Testing Goat')

        francis_url = self.browser.current_url
        self.assertRegex(francis_url, '/lists/.+')
        self.assertNotEqual(francis_url, edith_url)

        page_content = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Read OS', page_content)
        self.assertNotIn('Write songs', page_content)
