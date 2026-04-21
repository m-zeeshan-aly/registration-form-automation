from playwright.sync_api import Page, expect
import os
class RegistrationPage:
    # INPUT_BY_PLACEHOLDER = '//input[@placeholder="{label}"]'
    # Targets ANY element that is either an input or a textarea, 
    # provided it has the matching placeholder attribute.
    DYNAMIC_FIELD_XPATH_INPUT = '//*[(self::input or self::textarea) and @placeholder="{label}"]'
    DYNAMIC_FIELD_XPATH_RADIO = '//input[@type="radio" and @value="{value}"]'
    # Updated Template for Checkboxes
    DYNAMIC_CHECKBOX_BY_LABEL = "//div[label[normalize-space()='{label}']]//input[@type='checkbox']"

    # Finds the dropdown container by its ID (state or city)
    DYNAMIC_DROPDOWN_CONTAINER = "//div[@id='{id_name}']"

    # Finds the option inside the list once it opens
    DYNAMIC_DROPDOWN_OPTION = "//div[@role='option' and text()='{option_text}']"

    # Templates for the Date Picker components
    DATE_INPUT = "//input[@id='dateOfBirthInput']"
    # Unified template for ANY select dropdown in the date picker
    DATE_SELECT_TEMPLATE = "//select[@class='react-datepicker__{type}-select']"
    # Template for the specific day in the grid
    DAY_TEMPLATE = "//div[contains(@class, 'react-datepicker__day--{day}') and not(contains(@class, 'outside-month'))]"
    def __init__(self, page: Page):
        self.page = page
 
        # Subjects
        self.subjects_input = page.locator("//input[@id='subjectsInput']")

        # File upload
        self.file_picture_upload = page.locator("//input[@id='uploadPicture']")

        # Submit button
        self.submit_btn = page.locator("//button[@id='submit']")
    
    def navigate(self):
        # 1. Action: Navigate
        self.page.goto("https://demoqa.com/automation-practice-form")

        # 2. Verification: Check the URL
        # We use 'expect' so Playwright waits for the URL to change
        expect(self.page).to_have_url("https://demoqa.com/automation-practice-form")

        # 3. Verification: Check a Page Heading
        # This is the "Gold Standard" for verifying you are on the right page
        page_heading = self.page.locator("h1, .main-header")
        expect(page_heading).to_have_text("Practice Form")

    print("Success: Verified arrival at the Registration Form page.")


    # ... This method can be reused for any field, making your code DRY (Don't Repeat Yourself)

    def fill_input(self, placeholder_text, value):
        # 1. Create a dynamic locator using the placeholder text
        input_locator = self.page.locator(self.DYNAMIC_FIELD_XPATH_INPUT.format(label=placeholder_text))
        
        # 2. Ensure the field is visible and enabled before interacting
        expect(input_locator).to_be_visible()
        expect(input_locator).to_be_enabled()
        
        # 3. Fill the field
        input_locator.fill(value)
        
        # 4. Verify the value was entered correctly
        expect(input_locator).to_have_value(value)
        print(f"Verified: '{value}' was correctly entered into the field with placeholder '{placeholder_text}'.")

    def fill_and_verify(self, locator, value):

        """Fills a field and immediately  after checking the filed is visiable
        enable and editable asserts that the value is correct."""

        expect(locator).to_be_visible()  # Ensure the field is visible before interacting
        expect(locator).to_be_enabled()  # Ensure the field is enabled before interacting
        expect(locator).to_be_empty()    # Ensure the field is empty before filling (optional, depends on your test case)
        expect(locator).to_be_editable()  # Ensure the field is editable before filling (optional, depends on your test case)
        # 1. Action: Fill the field
        locator.fill(value)
        
        # 2. Assertion: Verify the 'value' attribute of the input
        # In web forms, typed text is stored in the 'value' property
        expect(locator).to_have_value(value)
        print(f"Verified: {value} was correctly entered.")

    def select_gender_radio_button(self, value):
        radio_locator = self.page.locator(self.DYNAMIC_FIELD_XPATH_RADIO.format(value=value))
        radio_locator.check()
        expect(radio_locator).to_be_checked()
        print("Verified: Radio button is checked.")

    # Example of a method to check a checkbox
    def checks_verifies_checkbox(self, checkbox_locator):
        expect(checkbox_locator).to_be_visible()
        expect(checkbox_locator).to_be_enabled()  # Ensure it's enabled before interacting
        expect(checkbox_locator).not_to_be_checked()  # Ensure it's not checked before
        checkbox_locator.check()
        expect(checkbox_locator).to_be_checked()
        print("Verified: Checkbox is checked.")


    def check_checkboxs(self,checkbox_values):
        for checkbox_value in checkbox_values:
            checkbox_locator = self.page.locator(self.DYNAMIC_CHECKBOX_BY_LABEL.format(label=checkbox_value))
            self.checks_verifies_checkbox(checkbox_locator)
    
    def verify_date_ui(self, day, month, year):
        # --- 5. DYNAMIC VERIFICATION LOGIC ---
        # DemoQA displays the date in the input field as: "DD Mon YYYY" (e.g., 05 Apr 2026)
        
        # Format day to 2 digits for UI check (e.g., 5 -> "05")
        formatted_day_ui = str(day).zfill(2)
        
        # Format month to first 3 letters for UI check (e.g., "April" -> "Apr")
        short_month = month[:3] 
        
        # Construct the expected string
        expected_date_string = f"{formatted_day_ui} {short_month} {year}"
        
        # Get actual value from the input field
        actual_date_value = self.page.locator(self.DATE_INPUT).input_value()
        
        # Professional Assertion
        assert actual_date_value == expected_date_string, f"Date mismatch! Expected '{expected_date_string}' but found '{actual_date_value}'"
        
        print(f"Verified: Date of Birth successfully set to '{expected_date_string}'.")
        
    def select_dob(self, day, month, year):
        # 1. Open the Calendar
        self.page.locator(self.DATE_INPUT).click()

        # 2. Select Month (Dynamically find the month dropdown)
        month_xpath = self.DATE_SELECT_TEMPLATE.format(type="month")
        self.page.locator(month_xpath).select_option(label=month)

        # 3. Select Year (Dynamically find the year dropdown)
        year_xpath = self.DATE_SELECT_TEMPLATE.format(type="year")
        self.page.locator(year_xpath).select_option(value=str(year))

        # 4. Select Day
        # Handle the 3-digit padding required by React-Datepicker
        formatted_day = str(day).zfill(3)
        day_xpath = self.DAY_TEMPLATE.format(day=formatted_day)
        self.page.locator(day_xpath).click()

        # 5. Verification (Keep your existing logic)
        self.verify_date_ui(day, month, year)

    def select_dropdown_option_dynamically(self, dropdown_id, option_text):
        # Find the dropdown container
        dropdown_container = self.page.locator(self.DYNAMIC_DROPDOWN_CONTAINER.format(id_name=dropdown_id))
        expect(dropdown_container).to_be_visible()
        dropdown_container.click()

        # Find the option within the dropdown
        option_locator = self.page.locator(self.DYNAMIC_DROPDOWN_OPTION.format(option_text=option_text))
        expect(option_locator).to_be_visible()
        option_locator.click()

    def select_dropdown_option_dynamically_method_fill(self, dropdown_id, option_text):
        # Find the dropdown container
        dropdown_container = self.page.locator(self.DYNAMIC_DROPDOWN_CONTAINER.format(id_name=dropdown_id))
        expect(dropdown_container).to_be_visible()
        dropdown_container.click()

        self.page.keyboard.type(option_text)
        self.page.keyboard.press("Enter")
        expect(dropdown_container).to_contain_text(option_text)

    def upload_file(self, file_path, file_name):
        # 1. Ensure the file input is visible and enabled before interacting
        expect(self.file_picture_upload).to_be_visible()
        expect(self.file_picture_upload).to_be_enabled()
        # 1. Combine the folder path with the file name
        file_path = file_path + file_name

        # 2. Perform the upload 
        # REMINDER: Do not use .click() before this!
        self.file_picture_upload.set_input_files(file_path)

        # 3. Verification
        actual_value = self.file_picture_upload.input_value()
        assert file_name in actual_value
        print(f"Verified: File '{file_name}' uploaded successfully from absolute path.")


    def fill_form(self, fname, lname, email, phone_num , gender=None, subjects=None, hobbies=[], address=None, day=None, month=None, year=None, file_path=None, file_name=None, state=None, city=None, sate_city_selection_method=None):
        # Call your generic method for each field
        
        
        self.fill_input("First Name", fname)
        self.fill_input("Last Name", lname)
        self.fill_input("name@example.com", email)
        self.fill_input("Mobile Number", phone_num)

        # self.check_radio(self.gender_male)  # Example of selecting a radio button
        
        
        self.select_gender_radio_button("Male")
        self.select_gender_radio_button("Other")
        self.select_gender_radio_button("Female")
        self.select_gender_radio_button(gender)

       
        
        # This method takes a list of hobbies and checks the corresponding checkboxes
        self.check_checkboxs(hobbies)  # Example of checking multiple checkboxes

        # Fill the subjects field and verify it
        self.fill_and_verify(self.subjects_input, subjects)  # Example of filling the subjects field
        
        # Current address
        self.fill_input("Current Address", address)  # Example of filling the current address field using the dynamic locator method

        # selecting date of birth using the method we defined
        self.select_dob(day, month, year)  # Example of selecting a date of birth

        # Now you can call the file upload method with the path to your file
        self.upload_file(file_path, file_name)  # Example of uploading a file

        if sate_city_selection_method == "keyboard":
            self.select_dropdown_option_dynamically_method_fill("state", state)
            self.select_dropdown_option_dynamically_method_fill("city", city)
        elif sate_city_selection_method == "selecting_option":
            self.select_dropdown_option_dynamically("state", state)
            self.select_dropdown_option_dynamically("city", city)


        # Finally, submit the form
        expect(self.submit_btn).to_be_visible()
        expect(self.submit_btn).to_be_enabled()
        self.submit_btn.click()  # Finally, submit the form