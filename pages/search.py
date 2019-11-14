"""
This module contains IndeedSearchPage,
the page object for the Indeed search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class IndeedSearchPage:
  
  URL = 'https://jp.indeed.com'

  SEARCH_INPUT = (By.ID, 'text-input-what')

  def __init__(self, browser):
    self.browser = browser

  def load(self):
    self.browser.get(self.URL)

  def search(self, phrase):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.send_keys(phrase + Keys.RETURN)
