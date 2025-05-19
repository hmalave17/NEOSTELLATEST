import os
from pytest_bdd import scenarios, given, when, then  

from src.test.hooks.DataReader import DataReader
from src.test.pages.login_page import LoginPage
from src.test.pages.form_page import FormPage
from src.test.pages.summary_page import SummaryPage

scenarios('../../resource/features/challenge.feature')

login_page = None
form_page = None
summary_page = None
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../resource/data/challenge.xlsx'))
data = DataReader.get_users(data_path)

@given("user open url")
def open_url(page):
    global login_page
    global form_page
    global summary_page
    login_page = LoginPage(page)
    form_page = FormPage(page)
    summary_page = SummaryPage(page)
    login_page.open()
    login_page.login()

@when("user sends 50 forms")
def step_send_forms():
    form_page.fill_form(data)

@then("user ends the challenge")
def step_complete_challenge():
    assert summary_page.verify_success_message()
    assert summary_page.verify_time_challenge()
