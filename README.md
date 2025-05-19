## Project
The NEOSTELLATEST automation project was created to demonstrate the automation testing skills of Hernan José Malave Montero, who is interested in becoming a part of Neostella.

## characteristics
This project has the following key features:
Programming Language: Python
Automation Framework: Playwright
Design Pattern: POM (Page Object Model)
Note: This project is designed to run on Windows machines and uses the Chrome browser by default.

## Project Structure

NEOSTELLATEST<br>
├─ src<br>
│ ├─ resource<br>
│ │ ├─ data<br>
│ │ │ └─ challenge.xlsx<br>
│ │ └─ features<br>
│ │ └─ challenge.feature<br>
│ │<br>
│ └─ test<br>
│ ├─ functions<br>
│ │ ├─ init.py<br>
│ │ ├─ constants.py<br>
│ │ ├─ logger.py<br>
│ │ ├─ system_message.py<br>
│ │ └─ utility_functions.py<br>
│ │<br>
│ ├─ hooks<br>
│ │ ├─ ConfigUrl.py<br>
│ │ ├─ DataReader.py<br>
│ │ └─ Page.py<br>
│ │<br>
│ ├─ pages<br>
│ │ ├─ form_page.py<br>
│ │ ├─ login_page.py<br>
│ │ └─ summary_page.py<br>
│ │<br>
│ └─ tests<br>
│ ├─ conftest.py<br>
│ └─ test_challenge.py<br>
│<br>
├─ .gitignore<br>
└─ playwright.config.py<br>

**File List:**  
- **challenge.xlsx:** Contains the test data for the challenge.<br>
- **challenge.feature:** Contains the BDD (Behavior-Driven Development) features for the project.<br>
- **init.py:** Initializes the function modules in the functions directory.<br>
- **constants.py:** Stores constant values used across the automation scripts.<br>
- **logger.py:** Handles logging and console output.<br>
- **system_message.py:** Stores system messages, including error, info, and debug messages.<br>
- **utility_functions.py:** Contains helper methods for various automation tasks.<br>
- **ConfigUrl.py:** Sets the environment URLs (e.g., QA) for the tests.<br>
- **DataReader.py:** Reads test data from external sources.<br>
- **Page.py:** Initializes the Page Object Model (POM) pages.<br>
- **form_page.py, login_page.py, summary_page.py:** These files represent the page objects where methods and elements are declared, following the POM architecture.<br>
- **conftest.py:** Pytest configuration file for setting up test fixtures and hooks.<br>
- **test_challenge.py:** Contains the test cases written using Pytest.<br>
- **.gitignore:** Specifies which files and directories should be ignored by Git to avoid unnecessary clutter in the repository.<br>
- **playwright.config.py:** Contains the Playwright configuration for the project.<br>

## execution
**steps to run project :**  
1. git clone https://github.com/hmalave17/NEOSTELLATEST.git<br>
2. cd NEOSTELLATEST<br>
3. pytest -s<br>



