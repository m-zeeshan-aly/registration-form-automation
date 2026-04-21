# Registration Form Playwright Automation

## 📋 Project Overview

This project is an automated testing suite for a **Practice Registration Form** built using **Playwright** and **pytest**. It demonstrates comprehensive automated UI testing with form interactions, validations, and file uploads.

The test suite automates filling out a complex registration form on [DemoQA](https://demoqa.com/automation-practice-form) with various input types including:
- Text fields (First Name, Last Name, Email, Phone)
- Radio buttons (Gender)
- Checkboxes (Hobbies)
- Date picker (Date of Birth)
- Text area (Address)
- File upload (Picture)
- Dropdown selectors (State and City)
- Form submission

## 🎯 What This Project Does

The automation suite:
1. **Generates** random, realistic test data using the **Faker** library
2. **Runs stress tests** by executing the same test multiple times with different data sets
3. **Navigates** to the DemoQA Practice Form
4. **Fills** all form fields with dynamically generated test data
5. **Validates** each field after interaction (visibility, enabled state, correct values)
6. **Selects** dates from a date picker component using random date generation
7. **Uploads** files to the form
8. **Selects** options from dropdown menus with proper state-city relationships
9. **Submits** the completed form
10. **Verifies** all interactions were successful

This project serves as a practical example of:
- The **Page Object Model (POM)** pattern for maintainable test code
- **Data-driven testing** using parametrization for stress testing
- **Faker library** integration for realistic test data generation
- Best practices for Playwright automation with pytest
- Form field interactions and validations
- Proper test setup and teardown
- Dynamic test execution with multiple iterations

## 📦 Prerequisites

- **Python 3.11+** installed on your system
- **pip** (Python package manager)
- **Git** (optional, for cloning the repository)

## 🚀 Installation & Setup

### 1. Clone or download the project
```bash
git clone <repository-url>
cd registrationFormPlaywright
```

### 2. Create a Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv signupPythonPlayWrightEnv

# Activate the virtual environment
# On Linux/Mac:
source signupPythonPlayWrightEnv/bin/activate

# On Windows:
signupPythonPlayWrightEnv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- **Playwright** - Browser automation library
- **pytest** - Testing framework
- **pytest-playwright** - Pytest plugin for Playwright
- **pytest-base-url** - Base URL fixture for pytest
- **Faker** - Library for generating realistic test data (names, emails, addresses, phone numbers, etc.)

### 4. Install Playwright Browsers
```bash
playwright install
```

This downloads the necessary browser binaries (Chromium, Firefox, WebKit).

## ▶️ Running the Tests

### Run all tests with default settings (headed browser)
```bash
pytest
```

The test will run with:
- 🌐 **Headed browser** (you'll see the browser window)
- ⏱️ **Slowed down execution** (500ms delay between actions for visibility)
- 📺 **Console output** enabled to see print statements

### Run tests with custom options

```bash
# Run in headless mode (without seeing the browser)
pytest --headless

# Run with a specific browser
pytest --browser firefox

# Run without slowdown
pytest -o addopts=""

# Run with output capture disabled (see all print statements)
pytest -s

# Run a specific test
pytest tests/test_registration.py::test_full_registration

# Run with verbose output
pytest -v
```

### Run tests in headed mode with Firefox browser
```bash
pytest --headed --browser firefox
```

## 📁 Project Structure

```
registrationFormPlaywright/
├── conftest.py                 # Pytest configuration and fixtures
├── pytest.ini                  # Pytest settings and CLI defaults
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── pages/
│   └── registration_page.py    # Page Object Model for the registration form
│
├── tests/
│   └── test_registration.py    # Test cases for form automation (parametrized for multiple iterations)
│
├── utils/
│   └── data_generator.py       # DataGenerator class using Faker for realistic test data
│
├── file_upload/
│   └── file_upload_example.jpeg # Sample file for upload test
│
└── signupPythonPlayWrightEnv/  # Virtual environment (created during setup)
```

## 🔧 Key Components

### `conftest.py`
- Defines pytest fixtures
- The `set_up` fixture initializes the browser page for each test
- Sets viewport size to 1280x720 for consistent testing

### `pytest.ini`
- Configures default pytest options
- Sets browser to Chromium with headed mode
- Adds 500ms slowdown for visibility
- Enables console output

### `utils/data_generator.py` 🆕
**DataGenerator class for dynamic test data:**
- Uses **Faker** library to generate realistic test data
- `get_registration_data()` - Returns a dictionary with random:
  - First and last names
  - Email addresses
  - Phone numbers (Indian format)
  - Gender (Male, Female, Other) - **Capitalized for use with dynamic XPath selectors**
  - Date of birth (ages 18-60)
  - Addresses with proper formatting
  - Subjects and hobbies
  - State and city with proper relationships (state-city mapping)
  - File path and upload filename
  - **State/City selection method** - Randomly chooses between "keyboard" or "selecting_option" strategies
- Ensures **state-city relationships** are realistic (e.g., Delhi with NCR, Lucknow with Uttar Pradesh)
- Each call generates completely new random data

### `pages/registration_page.py` - ✨ **Refactored with Dynamic XPath Templates**
**Dynamic XPath Templates (Class Constants):**
- `DYNAMIC_FIELD_XPATH_INPUT` - Selects input/textarea fields by placeholder text
- `DYNAMIC_FIELD_XPATH_RADIO` - Selects radio buttons by value
- `DYNAMIC_CHECKBOX_BY_LABEL` - Selects checkboxes by label text
- `DYNAMIC_DROPDOWN_CONTAINER` - Selects dropdown container by ID
- `DYNAMIC_DROPDOWN_OPTION` - Selects dropdown options by text with role='option'
- `DATE_SELECT_TEMPLATE` - Selects date picker dropdowns (month/year)
- `DAY_TEMPLATE` - Selects specific days in the calendar grid

**Key Methods:**
- `navigate()` - Navigates to the form and verifies successful navigation
- `fill_input()` - **NEW** - Dynamically fills input fields using placeholder text
- `fill_and_verify()` - Fills a field and validates the input
- `select_gender_radio_button()` - **REFACTORED** - Dynamically selects radio buttons by value
- `check_checkboxs()` - **REFACTORED** - Selects multiple checkboxes using dynamic labels
- `select_dob()` - **REFACTORED** - Uses dynamic date picker templates
- `verify_date_ui()` - **NEW** - Separated verification logic for date validation
- `upload_file()` - Handles file upload
- `select_dropdown_option_dynamically()` - **NEW** - Generic dropdown selection by clicking options
- `select_dropdown_option_dynamically_method_fill()` - **NEW** - Generic dropdown selection using keyboard
- `fill_form()` - Main method that orchestrates filling the entire form using dictionary unpacking

### `tests/test_registration.py`
**Main test case with stress testing approach:**
- `test_full_registration()` - Complete end-to-end registration form test
- **Parametrized** with `@pytest.mark.parametrize("iteration", range(1))` to run the test **1 time** (customizable for stress testing)
- Each iteration generates **completely new random data** via `DataGenerator`
- Uses **dictionary unpacking** (`**test_data`) to pass data to the form
- Each iteration uses a **randomly selected state/city selection method** for testing different UI interaction patterns
- Useful for stress testing and validating the application with multiple data sets and interaction strategies
- Print statements show which iteration and user data were processed

## 📊 Test Data - Dynamic Generation

**Instead of hardcoded data, the test suite now uses dynamic, realistic data generation:**

The `DataGenerator` class generates new random data for each test iteration:
```python
from utils.data_generator import DataGenerator

data_gen = DataGenerator()
test_data = data_gen.get_registration_data()
```

**Sample generated data structure:**
```python
{
    "fname": "John",                          # Random first name
    "lname": "Smith",                         # Random last name
    "email": "john.smith@example.com",        # Random email
    "phone_num": "9876543210",                # Random phone (10 digits)
    "gender": "Male",                         # Random gender (Male, Female, Other)
    "subjects": "Maths",                      # Fixed subject
    "hobbies": ["Sports", "Music"],           # Fixed hobbies
    "address": "123 Main St, City, Country",  # Random address
    "day": "15",                              # Random day (18-60 age range)
    "month": "March",                         # Random month (full name)
    "year": "1985",                           # Random year
    "file_path": "file_upload/",              # Upload directory
    "file_name": "file_upload_example.jpeg",  # Upload filename
    "state": "Haryana",                       # Random state
    "city": "Karnal",                         # City matching the state
    "sate_city_selection_method": "keyboard"  # Random method: "keyboard" or "selecting_option"
}
```

**Stress Testing:** The test runs **1 iteration** by default. To increase iterations for stress testing, modify:
```python
@pytest.mark.parametrize("iteration", range(5))  # Runs 5 times with different data each iteration
```

## ⚡ Stress Testing & Data Generation

### Dynamic Test Data with Faker
This project uses the **Faker** library to generate realistic, random test data:
- **Names:** Random first and last names
- **Emails:** Random email addresses
- **Phone Numbers:** Indian format phone numbers
- **Addresses:** Realistic multi-line addresses
- **Dates:** Random dates of birth (ages 18-60)
- **Locations:** State-city pairs with proper relationships

### Running Parametrized Tests (Stress Testing)
The test is parametrized to run **multiple iterations** with different data each time:

```bash
# Run tests (default 1 iteration)
pytest -s

# Each iteration uses NEW random data and a randomly selected state/city selection method
# Example output:
# Completed iteration 1 with user: John (keyboard method)
```

### Customizing Test Iterations
Modify the number of test iterations in [tests/test_registration.py](tests/test_registration.py):

```python
# Current: runs 1 time
@pytest.mark.parametrize("iteration", range(1))

# Change to 5 iterations:
@pytest.mark.parametrize("iteration", range(5))

# Change to 10 iterations for heavier stress testing:
@pytest.mark.parametrize("iteration", range(10))
```

### Why This Approach?
✅ **DRY Principle** - Uses dynamic XPath templates instead of hardcoded locators  
✅ **Reusable Methods** - Generic functions work with any field using placeholders/IDs  
✅ **Maintainable** - Single method definition handles multiple form fields  
✅ **Scalable** - Add new fields without creating new methods  
✅ **Flexible** - Supports multiple interaction strategies (keyboard vs clicking)  
✅ **Comprehensive Testing** - Tests with multiple data variations and interaction methods

## 🎯 Dynamic XPath Template Approach

Instead of hardcoding individual methods for each field, the refactored code uses **parameterized XPath templates**:

### **Dynamic Input Fields** (`DYNAMIC_FIELD_XPATH_INPUT`)
```python
# Uses placeholder text to find fields dynamically
self.fill_input("First Name", "John")
self.fill_input("Last Name", "Doe")
self.fill_input("Current Address", "123 Main St")
# Works with ANY input or textarea field with a matching placeholder
```

### **Dynamic Radio Buttons** (`DYNAMIC_FIELD_XPATH_RADIO`)
```python
# Uses value attribute to select radio buttons dynamically
self.select_gender_radio_button("Male")
self.select_gender_radio_button("Female")
self.select_gender_radio_button("Other")
```

### **Dynamic Checkboxes** (`DYNAMIC_CHECKBOX_BY_LABEL`)
```python
# Selects checkboxes by their label text
self.check_checkboxs(["Sports", "Music"])
# Works with ANY checkbox with a matching label
```

### **Dynamic Dropdown Selection** (Two Methods)
**Method 1 - Clicking Options:**
```python
self.select_dropdown_option_dynamically("state", "Haryana")
# Opens dropdown by ID, finds and clicks option by text
```

**Method 2 - Keyboard Input:**
```python
self.select_dropdown_option_dynamically_method_fill("city", "Karnal")
# Opens dropdown, types value, and presses Enter
```

Each test iteration randomly selects between these methods for testing different UI interaction patterns.

## 🐛 Troubleshooting

### Tests fail with "browser not found"
```bash
# Reinstall Playwright browsers
playwright install chromium
```

### Virtual environment not activating
Ensure you're in the correct project directory and check the path syntax for your OS.

### File upload fails
Verify the file path in the test:
- Update `file_path` to point to your `file_upload/` directory
- Ensure the file exists: `/home/ibraheem/Music/vfairs/registrationFormPlaywright/file_upload/file_upload_example.jpeg`

### Tests run too slowly or too fast
Edit `pytest.ini` and adjust the `--slowmo` value (in milliseconds):
```ini
addopts = --headed --browser chromium --slowmo 1000 -s
```

## 📝 Best Practices Demonstrated

1. **Page Object Model** - Separates test logic from page interactions
2. **Assertions with Playwright expect()** - Clear, readable validations
3. **DRY Principle** - Reusable methods like `fill_and_verify()`
4. **Explicit Waits** - Using `expect()` for proper synchronization
5. **Test Fixtures** - Using pytest fixtures for test setup/teardown
6. **Documentation** - Clear comments explaining complex interactions

## 🔗 Useful Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [pytest Documentation](https://docs.pytest.org/)
- [DemoQA Practice Form](https://demoqa.com/automation-practice-form)
- [Page Object Model Pattern](https://playwright.dev/python/docs/pom)

## 📄 License

This project is provided as-is for educational and testing purposes.

---

**Happy Testing! 🎉**
