import os

URL_ENV = {
    "LOCAL": "",
    "DEFAULT": "",
    "DEV": "",
    "QA": "https://www.theautomationchallenge.com/",
    "PDN": "",
}

#Get the environment from the environment variables, or use 'DEFAULT'.
environment = os.getenv("URL", "QA")
base_url = URL_ENV.get(environment, environment)

URLS = {
    "BASE_URL": base_url
}