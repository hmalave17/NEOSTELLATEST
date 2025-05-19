import re
import random
from playwright.sync_api import Locator
from src.test.functions.system_message import SystemMessage

class UtilityFunctions:

    #this method  return a email dinacmic
    @staticmethod
    def generate_dynamic_email(name: str, last_name: str) -> str:
        random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        return f"{name}{random_numbers}{last_name}@gmail.com"

    #this method  return a Locator dinacmic 
    @staticmethod
    def get_input_by_label(self, label_text: str) -> Locator:
        return self.page.locator(".bubble-r-box").filter(
            has=self.page.locator(".bubble-element.Text .content", has_text=re.compile(fr"^{label_text}$"))
        ).locator("input").filter(visible=True)
    
    #this method  complete valueData
    @staticmethod
    def complete_valueData(valueData, data):
        expected_labels = ["EIN", "Company Name", "Sector", "Address", "Automation Tool", "Annual Saving", "Date"]        
        for label in expected_labels:
            if label in data and label not in valueData:  
                valueData.append(data[label])
        while len(valueData) < 7:
            valueData.append("Value not available") 
        return valueData

    #this method retorn the execution time as a number 
    @staticmethod
    def get_completion_time(success_rate_box: Locator) -> float:
        text = success_rate_box.text_content().strip()
        match = re.search(r"\d+\.\d+", text)
        if match:
            return float(match.group(0))
        raise ValueError(SystemMessage.TIME_MESSAGE_ERROR)