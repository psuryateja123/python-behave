import random

from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from utils_pages.actions import elementActions

author = 'surya pulakhandam'

class github_search_objects(object):
    home_page_url = 'https://github.com/'
    search_tab = '/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label'
    search_results = '//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[1]/h3/a'

class github_search_pageObjects(elementActions):
    url = github_search_objects.home_page_url

    def click_on_search(self):
        self.click_by_xpath(github_search_objects.search_tab)

    def type_in_search(self):
        self.find_by_xpath(github_search_objects.search_tab).text()

    def fill_text_search(self):
        self.fill_text_search_by_xpath(github_search_objects.search_tab, "psuryateja123/python-behave")

    def hit_enter(self):
        v = self.find_by_xpath(github_search_objects.search_tab)
        v.send_keys(Keys.ENTER)

    def find_text_in_search_results(self):
        self.find_by_class(github_search_objects.search_results).text()

    def checking_for_repo(self):
        self.assertEquals(github_search_pageObjects.find_text_in_search_results, "psuryateja123/python-behave")

    def selecting_the_repo(self):
        self.click_by_xpath(github_search_objects.search_results)
