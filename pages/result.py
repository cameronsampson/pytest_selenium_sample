"""
This module contains IndeedResultPage,
the page object for the Indeed search result page.
"""

from selenium.webdriver.common.by import By


class IndeedResultPage:
  
  LINK_DIVS = (By.CSS_SELECTOR, '#resultsCol > div.jobsearch-SerpJobCard')
  SEARCH_INPUT = (By.ID, 'what')

  @classmethod
  def PHRASE_RESULTS(cls, phrase):
    # need to figure out the proper xpath for this to pass
    xpath = f"//div[@class='result']//*[contains(text(), '{phrase}')]"
    return (By.XPATH, xpath)

  def __init__(self, browser):
    self.browser = browser

  def link_div_count(self):
    link_divs = self.browser.find_elements(*self.LINK_DIVS)
    return len(link_divs)

  def phrase_result_count(self, phrase):
    phrase_results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
    return len(phrase_results)
  
  def search_input_value(self):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    return search_input.get_attribute('value')
