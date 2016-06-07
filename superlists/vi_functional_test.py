from selenium import webdriver

import unittest


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')

        self.fail('Finish the test!')

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                input.get_attribute('placeholder'),
                'Enter a to-do item'
                )
        inputbox.send_keys("buy peacock feathers")
        inputbox.send_keys("\n")

if __name__ == '__main__':
    unittest.main(warnings='ignore')


