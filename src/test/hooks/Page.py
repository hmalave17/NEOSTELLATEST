from playwright.sync_api import Page
import logging


class PageManager:
    _global_page: Page = None

    @staticmethod
    def initialize_page(page: Page):
        PageManager._global_page = page

    @staticmethod
    def get_page() -> Page:
        if not PageManager._global_page:
            logging.warning("ERROR: Page is not initialized. Run PageManager.initialize_page() in a setup method.")
        return PageManager._global_page