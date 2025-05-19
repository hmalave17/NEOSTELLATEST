import pandas as pd

class DataReader:
    @staticmethod
    def get_users(file_path: str) -> list[dict]:
        df = pd.read_excel(file_path, engine='openpyxl')

        #Rename the columns to match the expected fields
        df = df.rename(columns={
            'company_name': 'Company Name',
            'company_address': 'Address',
            'employer_identification_number': 'EIN',
            'sector': 'Sector',
            'automation_tool': 'Automation Tool',
            'annual_automation_saving': 'Annual Saving',
            'date_of_first_project': 'Date'
        })

        #Convert each row into a dictionary
        users = df.to_dict(orient='records')
        
        #Replace NaN, 'n/a' and empty values with 'Unknown'.
        for user in users:
            for key, value in user.items():
                if pd.isna(value) or str(value).strip().lower() in ["n/a", ""]:
                    user[key] = "not applicable" 


        return users
