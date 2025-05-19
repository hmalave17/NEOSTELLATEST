from playwright.sync_api import Page, Locator
from src.test.hooks.ConfigUrl import URLS
from src.test.functions.constants import NAME, LAST_NAME, PASSWORD
from src.test.functions.utility_functions import UtilityFunctions

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.utiliyFunctions = UtilityFunctions
        self.login_button: Locator = page.locator("[tabindex='14']")
        self.sign_button: Locator = page.locator("[tabindex='23']")
        self.start_button: Locator = page.get_by_role("button", name="Start")
        self.first_name_input: Locator = page.get_by_placeholder("First Name")
        self.last_name_input: Locator = page.get_by_placeholder("Last Name")
        self.email_input: Locator = page.get_by_placeholder("Email")
        self.password_input: Locator = page.get_by_placeholder("Password")

    
    def open(self):
        self.page.goto(f"{URLS['BASE_URL']}")

    #This method makes login
    def login(self):
        self.login_button.click()
        self.first_name_input.type(NAME)
        self.last_name_input.type(LAST_NAME)
        self.email_input.type(self.utiliyFunctions.generate_dynamic_email(NAME, LAST_NAME))
        self.password_input.type(PASSWORD)
        self.sign_button.click()
        self.start_button.click()

