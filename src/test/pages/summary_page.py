from playwright.sync_api import Page, Locator, expect
from src.test.functions.system_message import SystemMessage
from src.test.functions.utility_functions import UtilityFunctions
from src.test.functions.logger import Logger



class SummaryPage:

    def __init__(self, page: Page):
        self.page = page
        self.logger = Logger("test_logs.log")  
        self.utiliyFunctions = UtilityFunctions
        self.success_message: Locator = page.get_by_text('SUCCESS!')
        self.success_rate_box = page.locator(".bubble-r-box .content strong").filter(visible=True)

    #This method checks the success message at the end of the test. 
    def verify_success_message(self):
        try:
            expect(self.success_message).to_be_visible()
            self.logger.info(SystemMessage.CHALLENGE_COMPLETED)
            return True
        except AssertionError:
            self.logger.info(SystemMessage.MESSAGE_NOT_FOUND)
            return False  

    #This method checks the time test message the end of the test. 
    def verify_time_challenge(self):
        actual_time = self.utiliyFunctions.get_completion_time(self.success_rate_box)
        time = 460.000 - actual_time
        if time > 0:
            self.logger.info(SystemMessage.TIME_VALIDATION_SUCCESS)
            return True  
        else:
            self.logger.info(SystemMessage.TIMEOUT_ERROR)
            return False  
