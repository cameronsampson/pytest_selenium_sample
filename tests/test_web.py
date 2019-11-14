"""
This module contains web test cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

import pytest

from pages.result import IndeedResultPage
from pages.search import IndeedSearchPage


def test_basic_Indeed_search(browser):
  # Set up test case data
  PHRASE = 'QA エンジニア'

  # Search for the phrase
  search_page = IndeedSearchPage(browser)
  search_page.load()
  search_page.search(PHRASE)

  # Verify that results appear
  result_page = IndeedResultPage(browser)
  assert result_page.link_div_count() > 0
  assert result_page.phrase_result_count(PHRASE) > 0
  assert result_page.search_input_value() == PHRASE
