
from src.test.hooks.ConfigUrl import URLS

base_config = {
    "base_url": URLS["BASE_URL"],
    "trace": "on",
    "headless": True,
    "color_scheme": "light",
    "action_timeout": 10000,
    "video": "retain-on-failure",
    "screenshot": "only-on-failure",
    "viewport": {"width": 1366, "height": 720},
    "ignore_https_errors": True,
    "launch_options": {
        "args": ["--disable-web-security"],
    },
}