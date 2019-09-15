from selenium.webdriver import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import webdriver_manager

author = 'surya pulakhandam'

import logging
from nose.tools import assert_true

from selenium.webdriver.common.by import By

class elementActions(object):

   def __init__(self, driver):
       self.driver = driver

    # defination to fill a form using css
   def fill_form_by_css(self, form_css, value):
       elem = self.driver.find_element_by_css_selector(form_css)
       elem.send_keys(value)

   # defination to fill a form using id
   def fill_form_by_id(self, form_element_id, value):
       return self.fill_form_by_css('#%s' % form_element_id, value)

   # defination to navigate to a specific URL
   def navigate(self):
       self.driver.get(self.url)

   # defination to click on an element using class
   def click_class(self, form_element_class):
       click_element = self.driver.find_element_by_class_name(form_element_class)
       click_element.click()

   # defination to click on an element using xpath
   def click_by_xpath(self, form_element_xpath):
       click_element_by_xpath = self.driver.find_element_by_xpath(form_element_xpath)
       click_element_by_xpath.click()

   # defination to click on an element using ID
   def click_by_id(self, form_element_id):
       click_element_by_id = self.driver.find_element_by_id(form_element_id)
       click_element_by_id.click()

   # defination to find element by using ID
   def find_by_id(self, element_id):
       find_element_by_id = self.driver.find_element_by_id(element_id)
       return find_element_by_id

   # defination to find element by using Xpath
   def find_by_xpath(self, element_xpath):
       find_element_by_xpath = self.driver.find_element_by_xpath(element_xpath)
       return find_element_by_xpath

   # defination to find element by using class
   def find_by_class(self,element_class_name):
       find_by_classname = self.driver.find_element_by_class_name(element_class_name)
       return find_by_classname

   # defination to assert an element using Xpath
   def assert_by_xpath(self, element_assert_xpath):
       assert_element_xpath = self.driver.find_element_by_xpath(element_assert_xpath)
       assert_true(assert_element_xpath)

   # defination to click on an element using css
   def click_by_css_selector(self, form_element_name):
       click_by_element_css = self.driver.find_element_by_css_selector(form_element_name)
       click_by_element_css.click()

   # defination to assert an element using class
   def assert_by_class(self,element_class):
        assert_element_by_class = self.driver.find_element_by_class_name(element_class)
        assert_true(assert_element_by_class)

   # defination to assert element by ID
   def assert_by_id(self,element_assert_id):
        assert_element_by_id = self.driver.find_element_by_id(element_assert_id)
        assert_true(assert_element_by_id)

   # defination to compare to elements
   def assertEquals(self, var1, var2):
       if var1 == var2:
           return True
       else:
           return False

   # defination to find element by CSS
   def find_by_css(self, element_css):
       find_element_by_css = self.driver.find_element_by_css_selector(element_css)
       return find_element_by_css

   # defination to find element by Name
   def find_name(self, form_element_name):
       find_by_name = self.driver.find_element_by_name(form_element_name)
       return find_by_name

   # defination to click element by element name
   def click_by_element_name(self, element_name):
       click_element_by_name = self.driver.find_element_by_name(element_name)
       click_element_by_name.click()

   # defination to assert element by partial text
   def assert_by_partial_text(self, element_partial_text):
       assert_element_by_partial_text = self.driver.find_element_by_partial_link_text(element_partial_text)
       assert_true(assert_element_by_partial_text)

   # defination to find element by partial text
   def find_by_partial_text(self, find_element_partial_text):
       find_element_by_partial_text = self.driver.find_element_by_partial_link_text(find_element_partial_text)
       return find_element_by_partial_text

   def enter_key(self):
       enter = self.driver.find_element_by_name("Value").send_keys(Keys.RETURN)
       return enter

     # defination to find element by partial text
   def find_by_link_text(self, find_element_link_text):
       find_element_by_linked_text = self.driver.find_element_by_link_text(find_element_link_text)
       return find_element_by_linked_text

   def find_by_tag(self, find_element_tag_text):
       find_element_by_tag = self.driver.find_element_by_tag_name(find_element_tag_text)
       return find_element_by_tag

   def fill_text(self, text, search_text):
       element_id = self.find_by_id(text)
       element_id.send_keys(search_text)

   def equals_key(self):
       equals = self.driver.find_element_by_id('toggle-hamburger-menu')
       equals.send_keys(Keys.EQUALS)
       equals.send_keys(Keys.EQUALS)

   def class_name(self, element_class_name):
       find_by_class_name = self.driver.findElement(By.cssSelector(element_class_name))
       return find_by_class_name

   def scroll_to(self, scroll_to_element):
       actions = ActionChains(driver)
       actions.move_to_element(scroll_to_element)
       actions.perform()

   def fill_text_search_by_xpath(self, text, search_text):
       element_xpath = self.find_by_xpath(text)
       element_xpath.send_keys(search_text)


