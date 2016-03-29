'''
Created on 2016年3月24日

@author: lyt
'''
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://www.baidu.com/')

  

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()


import unittest

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.yahoo.com')
        self.assertIn('Yahoo', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)