from playwright.sync_api import Page, Locator, TimeoutError
from src.test.functions.logger import Logger
from src.test.functions.system_message import SystemMessage
from src.test.functions.utility_functions import UtilityFunctions

class FormPage: 

    def __init__(self, page: Page):
        self.page = page
        self.logger = Logger("test_logs.log")  
        self.systemMessage = SystemMessage
        self.utiliyFunctions = UtilityFunctions
        self.submit_button: Locator = page.get_by_role("button", name="Submit")
        self.success_message: Locator = page.get_by_text('SUCCESS!')
        self.success_rate_box = page.locator(".bubble-r-box .content strong").filter(visible=True)

    #This method receives a list and iterates through it, sending the object that will be the form's data.
    def fill_form(self, data_list: list[dict]):
        if not data_list:
            raise Exception(SystemMessage.LIST_EMPTY)
        for i, data in enumerate(data_list):
            self.logger.info(SystemMessage.format(SystemMessage.FORM_SENDING, num=i + 1, data=data))
            self.send_form(data)

    #this method receives the form,  first loops it, and it does two things: 
    # The first sets a string in the locators to interact with them, and the other is to capture 
    # the values that we will send in those inputs. Then it evaluates if "values" is less than 7. 
    # We start to interact with the elements when they are visible and validate if the reCAPTCHA 
    # is present before filling in the input. Finally, it clicks on submit
    def send_form(self, data: dict):
        all_inputs = []
        valueData = []
        for label, value in data.items():
            if not value.strip():
                self.logger.info(SystemMessage.format(SystemMessage.MISSING_FIELD, label=label))
                continue
            inputs = self.utiliyFunctions.get_input_by_label(self, label)
            count = inputs.count()
            valueData.append(value)
            if count == 0:
                raise Exception(SystemMessage.format(SystemMessage.FORM_ERROR, num=i + 1, error=data))

        if len(valueData) < 7:
            valueData = self.utiliyFunctions.complete_valueData(valueData, data)

        for index, value in enumerate(valueData):
            self.logger.debug(SystemMessage.format(SystemMessage.DEBUG_INDEX_VALUE, index=index, value=value))

        for i in range(count):
            all_inputs.append((inputs.nth(i), valueData[i]))

        for input_field, value in all_inputs:
            try:
                input_field.wait_for(state="visible", timeout=5000)
                self.handle_recaptcha_popup()
                input_field.fill(value)
                self.logger.debug(SystemMessage.format(SystemMessage.DEBUG_INPUT_FILL, field=input_field, value=value))
            except Exception as e:
                self.logger.error(SystemMessage.SUBMIT_ERROR)          
        if all_inputs:
            self.submit_button.click()
            
            self.logger.info(SystemMessage.FORM_SEND_SUCCESSFUL)
        else:
            self.logger.error(SystemMessage.SUBMIT_ERROR)


    #this method checks if the recaptcha is present, 
    # if it is present, gives clicks on the checkbox, and waits two seconds for its state to change. 
    # if it cannot catch the element, it throws an exception. 
    # if the reCAPTCHA is not present, the system paints on the console a message popup not found.
    def handle_recaptcha_popup(self):
        try:
            popup = self.page.locator(".bubble-element.Popup").filter(visible=True)
            if popup.is_visible():
                self.logger.info(SystemMessage.RECAPTCHA_DETECTED)
                close_button = popup.locator(".bubble-element.Button.clickable-element")
                close_button.click(no_wait_after=True)
                self.logger.info(SystemMessage.RECAPTCHA_CLOSED)
                popup.wait_for(state="detached", timeout=2000)
            else:
                self.logger.info(SystemMessage.NO_FOUND_RECAPCHA)
        except TimeoutError:
            self.logger.error(SystemMessage.DEBUG_RECAPCHA)


