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
1. **Navigates** to the DemoQA Practice Form
2. **Fills** all form fields with realistic test data
3. **Validates** each field after interaction (visibility, enabled state, correct values)
4. **Selects** dates from a date picker component
5. **Uploads** files to the form
6. **Selects** options from dropdown menus
7. **Submits** the completed form
8. **Verifies** all interactions were successful

This project serves as a practical example of:
- The **Page Object Model (POM)** pattern for maintainable test code
- Best practices for Playwright automation with pytest
- Form field interactions and validations
- Proper test setup and teardown

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
│   └── test_registration.py    # Test cases for form automation
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

### `pages/registration_page.py`
**Page Object containing:**
- `navigate()` - Navigates to the form and verifies successful navigation
- `fill_and_verify()` - Fills a field and validates the input
- `check_radio()` - Selects a radio button
- `check_checkboxs()` - Selects multiple checkboxes for hobbies
- `select_dob()` - Interacts with the date picker
- `upload_file()` - Handles file upload
- `select_state_and_city()` - Selects from dropdown menus
- `fill_form()` - Main method that orchestrates filling the entire form

### `tests/test_registration.py`
**Main test case:**
- `test_full_registration()` - Complete end-to-end registration form test
- Uses sample data for all form fields
- Validates each step of the form submission

## 📊 Test Data

The test uses the following sample data:
- **Name:** Muhammad Zeeshan
- **Email:** zeeshan@example.com
- **Phone:** 0320840239
- **Gender:** Male
- **Date of Birth:** 9 January 1970
- **Subjects:** Maths, Physics
- **Hobbies:** Sports, Reading
- **Address:** 123 Main St, Anytown
- **State:** Uttar Pradesh
- **City:** Lucknow
- **Picture:** file_upload_example.jpeg

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
