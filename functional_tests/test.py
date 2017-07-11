from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        ## <tr> </tr> specifies a row
        ## rows is a "list"
        self.assertIn(
            row_text,
            [row.text for row in rows], 
            f"New to-do item didn't appear in the table. Contents were:\n{table.text}"
        )

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
#        print(self.live_server_url)
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
        time.sleep(1)
        self.check_for_row_in_list_table('1: Read OS')
        
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        ## We have to redefine inputbox after the page updates
        inputbox.send_keys('Write songs')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        
        self.check_for_row_in_list_table('1: Read OS')
        self.check_for_row_in_list_table('2: Write songs')

        self.fail('Finish the test!')

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        
        # She visits that URL - her to-do list is still there.
        
        # Satisfied, she goes back to sleep
