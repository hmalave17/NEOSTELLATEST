import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

import pytest
from src.test.hooks.Page import PageManager  

@pytest.fixture(scope="session")
def playwright_instance():
    from playwright.sync_api import sync_playwright
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    PageManager.initialize_page(page)
    yield page
    page.close()
