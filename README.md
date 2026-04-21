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
3. **Navigates** to the DemoQA Practice Form (URL passed as parameter)
4. **Fills** all form fields with dynamically generated test data
5. **Validates** each field after interaction (visibility, enabled state, correct values)
6. **Selects** dates from a date picker component using random date generation
7. **Uploads** files to the form with post-upload verification
8. **Selects** options from dropdown menus with proper state-city relationships
9. **Submits** the completed form
10. **Verifies** form submission success with modal confirmation message
11. **Tests multiple interaction patterns** - randomly uses keyboard or click strategies for dropdowns

This project serves as a practical example of:
- The **Page Object Model (POM)** pattern with factory methods for better maintainability
- **Getter/Action Method Pattern** - separating locator creation from interactions
- **Data-driven testing** using parametrization for stress testing
- **Faker library** integration for realistic test data generation
- **Playwright best practices** including wait strategies and visibility checks
- **Assertion chaining** for cleaner, more readable test code
- Form field interactions and comprehensive validations
- Proper test setup and teardown with fixtures
- **Dynamic test execution** with multiple iterations and random strategies

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
  - **use_keyboard** - Boolean flag (True/False) to randomly select dropdown selection strategy
- Ensures **state-city relationships** are realistic (e.g., Delhi with NCR, Lucknow with Uttar Pradesh)
- Each call generates completely new random data

### `pages/registration_page.py` - ✨ **Advanced Refactoring with Getter Methods & Action Pattern**

**Dynamic XPath Templates (Class Constants):**
- `DYNAMIC_FIELD_XPATH_INPUT` - Selects input/textarea fields by placeholder text
- `DYNAMIC_FIELD_XPATH_RADIO` - Selects radio buttons by value
- `DYNAMIC_CHECKBOX_BY_LABEL` - Selects checkboxes by label text
- `DYNAMIC_DROPDOWN_CONTAINER` - Selects dropdown container by ID
- `DYNAMIC_DROPDOWN_OPTION` - Selects dropdown options by text with role='option'
- `DATE_SELECT_TEMPLATE` - Selects date picker month/year by type
- `DAY_TEMPLATE` - Selects specific days in the calendar grid

**Getter Methods (Factory Pattern):**
- `get_input(placeholder_text)` - Returns locator for input fields by placeholder
- `get_radio(value)` - Returns locator for radio buttons by value
- `get_checkbox(label)` - Returns locator for checkboxes by label
- `get_dropdown_container(dropdown_id)` - Returns dropdown container by ID
- `get_dropdown_option(option_text)` - Returns dropdown option by text
- `get_date_input()` - Returns date input field locator
- `get_date_select(type)` - Returns date picker month/year select
- `get_day_locator(day)` - Returns specific day with 3-digit formatting

**Action Methods:**
- `type_text(locator, value)` - **NEW** - Generic robust text input method
- `select_gender(gender_name)` - **NEW** - Select gender radio button
- `check_hobby(hobby_name)` - **NEW** - Check hobby checkbox with safety checks
- `select_dob(day, month, year)` - **REFACTORED** - Date selection with template getters
- `select_dropdown_by_type(dropdown_id, option_text)` - **NEW** - Keyboard-based dropdown selection
- `select_dropdown_by_click(dropdown_id, option_text)` - **NEW** - Click-based dropdown selection
- `verify_date_ui(day, month, year)` - Date verification with format checking
- `upload_file(file_path, file_name)` - File upload that returns locator for verification
- `navigate(url)` - **REFACTORED** - Now accepts URL as parameter
- `fill_form()` - **COMPLETELY REFACTORED** - Uses new methods with chained assertions and form submission verification

### `tests/test_registration.py`
**Main test case with improved data-driven approach:**
- `test_full_registration(page, iteration)` - Complete end-to-end registration form test
- **Parametrized** with `@pytest.mark.parametrize("iteration", range(1))` to run the test **1 time** (customizable for stress testing)
- Passes **URL as parameter** to the navigate method for flexibility
- Each iteration generates **completely new random data** via `DataGenerator`
- Uses **dictionary unpacking** (`**test_data`) to pass data to the form
- Each iteration uses a **randomly selected boolean flag** (use_keyboard) for different dropdown strategies
- Useful for stress testing and validating the application with multiple data sets and interaction methods
- Print statements show iteration progress and user data being tested

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
    "use_keyboard": True                      # Boolean flag: True (keyboard) or False (click)
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

## �️ Architecture: Getter Methods & Action Pattern

The code now follows a **two-layer pattern** for better separation of concerns and reusability:

### **Layer 1: Getter Methods (Locator Factories)**
These methods encapsulate XPath templates and return `Locator` objects. They keep template logic centralized:

```python
# Example getter methods - all return Locator objects
locator = page.get_input("First Name")           # Input field by placeholder
locator = page.get_radio("Male")                 # Radio button by value
locator = page.get_checkbox("Sports")            # Checkbox by label
locator = page.get_dropdown_container("state")   # Dropdown by ID
locator = page.get_day_locator(15)               # Day with 3-digit formatting
```

**Benefits:**
- XPath templates are defined once in constants
- Getters handle formatting (e.g., day padding to 3 digits)
- If DOM changes, only update the template constant
- Easy to debug and maintain

### **Layer 2: Action Methods (Robust Interactions)**
These methods perform UI interactions on locators and return them for assertion chaining:

```python
# Action methods handle visibility, state checks, and interactions
locator = page.type_text(input_locator, "John")          # Fill & verify text
locator = page.select_gender("Male")                     # Select gender radio
locator = page.check_hobby("Sports")                     # Check hobby checkbox
container = page.select_dropdown_by_click("state", "NC")  # Click dropdown option
container = page.select_dropdown_by_type("city", "Delhi")  # Keyboard dropdown
```

**Benefits:**
- Built-in visibility and state checks
- Error handling and wait strategies
- Returns locator for assertion chaining
- Consistent interaction patterns

### **Chaining Pattern in fill_form()**
The new refactored `fill_form()` method chains actions with assertions:

```python
# Locators are returned for assertion chaining
expect(self.type_text(self.get_input("First Name"), fname)).to_have_value(fname)
expect(self.select_gender(gender)).to_be_checked()
expect(self.select_dropdown_by_click("state", state)).to_contain_text(state)

# File upload also returns locator for verification
result = self.upload_file(file_path, file_name)
actual_value = result.input_value()
assert file_name in actual_value
```

**Benefits:**
- Clear, readable test code
- Immediate verification after each action
- Better error messages on failure
- Form submission modal verified at end

### **Dropdown Selection Strategies**

**Strategy 1: Keyboard Input** (`select_dropdown_by_type`)
```python
# Uses keyboard typing and Enter for speed
self.select_dropdown_by_type("state", "Haryana")
# Steps: Opens dropdown → Types value → Presses Enter
# Benefit: Fast, works across different browsers consistently
```

**Strategy 2: Click-based** (`select_dropdown_by_click`)
```python
# Uses mouse clicks on rendered options with visibility waits
self.select_dropdown_by_click("city", "Karnal")
# Steps: Opens dropdown → Waits for option → Clicks option
# Benefit: Handles animations, more reliable for complex dropdowns
```

Each test iteration **randomly uses one strategy** via the `use_keyboard` boolean flag for comprehensive testing of both approaches.

## ✨ Key Improvements in Latest Version

### **Getter/Action Pattern**
- **Before:** Direct locator creation in action methods, duplicated XPath logic
- **After:** Centralized getter methods for locator creation, action methods for interactions
- **Benefit:** Easier to maintain, single source of truth for selectors

### **Method Returns for Assertion Chaining**
- **Before:** Methods performed actions and verifications inline
- **After:** Methods return locators/containers for chaining with `expect()`
- **Benefit:** More readable test code, better error messages, immediate verification

### **Type-Safe Dropdown Selection**
- **Before:** Multiple method names (`_using_keyboard`, `_using_css`, `_using_xpath`)
- **After:** Two clear strategies: `select_dropdown_by_type()` (keyboard) vs `select_dropdown_by_click()` (click)
- **Benefit:** Simpler API, easier to understand intent

### **URL Parameter in navigate()**
- **Before:** URL hardcoded in `navigate()` method
- **After:** URL passed as parameter to `navigate(url)`
- **Benefit:** Flexible for testing multiple environments, reusable code

### **Form Submission Verification**
- **Before:** Only verified form submission button was clicked
- **After:** Verifies success modal appears with message "Thanks for submitting the form"
- **Benefit:** True end-to-end verification, confirms form was actually processed

### **Improved File Upload Verification**
- **Before:** Inline verification in upload method
- **After:** Method returns locator, verification in `fill_form()` with clear assertion
- **Benefit:** Better error handling, consistent with other methods

### **Boolean-based Strategy Selection**
- **Before:** String parameter `"keyboard"` vs `"selecting_option"`
- **After:** Boolean `use_keyboard` flag (True/False)
- **Benefit:** Simpler, clearer, less error-prone

## 💡 Usage Examples

### **Basic Form Filling**
```python
reg_page.navigate("https://demoqa.com/automation-practice-form")

# Data from data_generator
test_data = data_gen.get_registration_data()

# Fill form using dictionary unpacking
reg_page.fill_form(**test_data)
```

### **Using Getter Methods Directly**
```python
# Get locators for custom interactions
first_name_input = reg_page.get_input("First Name")
expect(first_name_input).to_be_visible()
reg_page.type_text(first_name_input, "John")

# Select gender
gender_radio = reg_page.select_gender("Male")
expect(gender_radio).to_be_checked()
```

### **Dropdown Selection with Different Strategies**
```python
# Using keyboard (faster)
if test_data["use_keyboard"]:
    reg_page.select_dropdown_by_type("state", "Haryana")
else:
    # Using click (more reliable for complex dropdowns)
    reg_page.select_dropdown_by_click("state", "Haryana")
```

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

1. **Page Object Model (POM)** - Separates test logic from page interactions
2. **Getter/Action Pattern** - Splits locator creation and interactions into two layers
3. **Assertions with Playwright expect()** - Clear, readable validations with assertion chaining
4. **Locator Return Pattern** - Methods return locators for assertion chaining
5. **DRY Principle** - Reusable methods like `type_text()` and `select_gender()`
6. **Explicit Waits** - Using `expect()` and `.wait_for()` for proper synchronization
7. **Test Fixtures** - Using pytest fixtures for test setup/teardown
8. **Form Submission Verification** - Confirms success modal appears after form submission
9. **Factory Methods** - Getter methods encapsulate XPath template logic
10. **Parametrized Tests** - Data-driven approach with random strategy selection

## 🔗 Useful Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [pytest Documentation](https://docs.pytest.org/)
- [DemoQA Practice Form](https://demoqa.com/automation-practice-form)
- [Page Object Model Pattern](https://playwright.dev/python/docs/pom)

## 📄 License

This project is provided as-is for educational and testing purposes.

---

**Happy Testing! 🎉**
