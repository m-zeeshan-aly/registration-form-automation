from playwright.sync_api import Page, expect
import os
class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator("//input[@id='firstName']")
        self.last_name = page.locator("//input[@id='lastName']")
        self.email = page.locator("//input[@id='userEmail']")
        self.phone = page.locator("//input[@id='userNumber']")
        # Radio buttons are usually selected by label
        self.gender_male = page.locator("//input[@id='gender-radio-1']")
        self.gender_female = page.locator("//input[@id='gender-radio-2']")
        self.gender_other = page.locator("//input[@id='gender-radio-3']")

        # Date of Birth
        self.dob_input = page.locator("//input[@id='dateOfBirthInput']")
        self.dob_year_dropdown = page.locator("//select[@class='react-datepicker__year-select']")
        self.dob_month_dropdown = page.locator("//select[@class='react-datepicker__month-select']")
        self.dob_days_table = page.locator("//div[@role='table']")

        self.dob_month_select = page.locator("//select[@class='react-datepicker__month-select']")

        # Subjects
        self.subjects_input = page.locator("//input[@id='subjectsInput']")

        # Checkboxes
        self.hobby_sports = page.locator("//input[@id='hobbies-checkbox-1']")
        self.hobby_reading = page.locator("//input[@id='hobbies-checkbox-2']")
        self.hobby_music = page.locator("//input[@id='hobbies-checkbox-3']")
        # File upload
        self.file_picture_upload = page.locator("//input[@id='uploadPicture']")
        # Address
        self.current_address = page.locator("//textarea[@id='currentAddress']")

        # State and City dropdowns
        self.state_dropdown = page.locator("//div[@id='state']")
        # self.state_options = page.locator("//div[@id='react-select-3-listbox']")  # Options within the state dropdown
        # self.state_option = page.locator("//div[@id='react-select-3-option-0']")  # Individual state options
        self.city_dropdown = page.locator("//div[@id='city']")  
        # self.city_options = page.locator("//div[@id='react-select-4-listbox']")  # Options within the city dropdown
        # self.city_option = page.locator("//div[@id='react-select-4-option-0']")  # Individual city options

        # These generic locators find ANY option inside the open menu
        self.menu_options = page.locator("div[id^='react-select-'][id*='-option']")
   
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

    # Example of a method to check a radio button
    def check_radio(self, radio_locator):
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
            if checkbox_value == "Sports":
                checkbox_locator = self.hobby_sports
            elif checkbox_value == "Reading":
                checkbox_locator = self.hobby_reading
            elif checkbox_value == "Music":
                checkbox_locator = self.hobby_music
            self.checks_verifies_checkbox(checkbox_locator)

    
    # In your class methods
    def select_dob(self, day, month, year):
        expect(self.dob_input).to_be_visible()
        expect(self.dob_input).to_be_enabled()  # Ensure it's not checked before
        
        self.dob_input.click()
       
        
        expect(self.dob_days_table).to_be_visible()
        
        # for month dropdown
        expect(self.dob_month_dropdown).to_be_visible()
        expect(self.dob_month_dropdown).to_be_enabled()
        self.dob_month_dropdown.click()
        # for month slecting
        self.dob_month_dropdown.select_option(label=month) # e.g., "April"
        
        # for year dropdown
        expect(self.dob_year_dropdown).to_be_visible()
        expect(self.dob_year_dropdown).to_be_enabled()
        self.dob_year_dropdown.click()

        # for year selecting
        self.dob_year_dropdown.select_option(value=year)   # e.g., "199

        # for day selecting
        formatted_day = str(day).zfill(3)  # Ensure day is two digits, e.g., "05" for 5th
        

        # 1. Format the number to be 3 digits (e.g., 5 becomes "005", 12 stays "012")
        formatted_day = str(day).zfill(3)
        
        # 2. Use an f-string to inject the formatted_day into your XPath
        xpath = f"//div[contains(@class, 'react-datepicker__day--{formatted_day}') and not(contains(@class, 'outside-month'))]"
        
        # 3. Execute the click
        self.page.locator(xpath).click()

        #verify the selected date
        # selected_date = self.dob_input.input_value()
        # expected_date = f"{formatted_day} {month} {year}"
        # assert selected_date == expected_date, f"Expected date to be '{expected_date}', but got '{selected_date}'"

        # print(f"Verified: Selected day {formatted_day} {month} {year} from the date picker.")


        # 2. Verification Logic (Matching the UI format: "DD Mon YYYY")
        # Format day to 2 digits (5 -> 05)
        formatted_day_ui = str(day).zfill(2)
        
        # Format month to first 3 letters (March -> Mar)
        short_month = month[:3] 
        
        selected_date = self.dob_input.input_value()
        expected_date = f"{formatted_day_ui} {short_month} {year}"
        
        # Use Playwright's built-in 'expect' for better error messages
        assert selected_date == expected_date, f"Expected '{expected_date}', but got '{selected_date}'"
        
        print(f"Verified: Date matches {expected_date}")


    def select_state_and_city_using_css_selecting_option(self, state, city):
        # --- 1. Select State ---
        expect(self.state_dropdown).to_be_visible()
        self.state_dropdown.click()
        
        # Locate the specific state option by its text and click it
        # We use .get_by_text(state, exact=True) to ensure we don't click 
        # "Uttar" if we wanted "Uttar Pradesh"
        state_to_click = self.page.get_by_text(state, exact=True)
        expect(state_to_click).to_be_visible()
        state_to_click.click()
        
        print(f"Clicked state option: {state}")

        # --- 2. Select City ---
        # The city dropdown usually takes a millisecond to become enabled 
        # after the state is selected.
        expect(self.city_dropdown).to_be_visible()
        self.city_dropdown.click()

        # Locate the specific city option by its text and click it
        city_to_click = self.page.get_by_text(city, exact=True)
        expect(city_to_click).to_be_visible()
        city_to_click.click()
        
        print(f"Clicked city option: {city}")

    

    def select_state_and_city_using_xpath_selecting_option(self, state, city):
        # --- 1. Select State ---
        expect(self.state_dropdown).to_be_visible()
        self.state_dropdown.click()
        
        # Dynamic XPath to find the option by its text
        # This looks for a div with the role 'option' that contains our state name
        state_option_xpath = f"//div[@role='option' and text()='{state}']"
        
        expect(self.page.locator(state_option_xpath)).to_be_visible()
        self.page.locator(state_option_xpath).click()
        
        print(f"XPath Verified: State '{state}' selected.")

        # --- 2. Select City ---
        expect(self.city_dropdown).to_be_visible()
        expect(self.city_dropdown).to_be_enabled()
        self.city_dropdown.click()

        # Dynamic XPath for the city option
        city_option_xpath = f"//div[@role='option' and text()='{city}']"
        
        expect(self.page.locator(city_option_xpath)).to_be_visible()
        self.page.locator(city_option_xpath).click()
        
        print(f"XPath Verified: City '{city}' selected.")



    def select_state_and_city_using_keyboard(self, state, city):
        # Click, type, and Enter for State

        expect(self.state_dropdown).to_be_visible()
        expect(self.state_dropdown).to_be_enabled()
        self.state_dropdown.click()
        self.page.keyboard.type(state)
        self.page.keyboard.press("Enter")
        expect(self.state_dropdown).to_contain_text(state)
        print(f"Verified: State '{state}' is displayed.")
        # expect(self.state_dropdown).to_have_text(state)  # Verify the selected state is displayed
        
        # Repeat for City
        expect(self.city_dropdown).to_be_visible()
        expect(self.city_dropdown).to_be_enabled()
        self.city_dropdown.click()
        self.page.keyboard.type(city)
        self.page.keyboard.press("Enter")
        expect(self.city_dropdown).to_contain_text(city)  # Verify the selected city is displayed
        print(f"Verified: State '{state}' and City '{city}' selected successfully.")



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
        
        self.fill_and_verify(self.first_name, fname)
        self.fill_and_verify(self.last_name, lname)
        self.fill_and_verify(self.email, email)
        self.fill_and_verify(self.phone, phone_num)

        self.check_radio(self.gender_male)  # Example of selecting a radio button
        self.check_radio(self.gender_female)
        self.check_radio(self.gender_other)

        # Conditainlally check the radio button based on the input parameter
        if gender == "male":
            self.check_radio(self.gender_male)
        elif gender == "female":
            self.check_radio(self.gender_female)
        elif gender == "other":
            self.check_radio(self.gender_other)
        
        # This method takes a list of hobbies and checks the corresponding checkboxes
        self.check_checkboxs(hobbies)  # Example of checking multiple checkboxes

        # Fill the subjects field and verify it
        self.fill_and_verify(self.subjects_input, subjects)  # Example of filling the subjects field
        
        # Current address
        self.fill_and_verify(self.current_address, address)  # Example of filling the current address field

        # selecting date of birth using the method we defined
        self.select_dob(day, month, year)  # Example of selecting a date of birth

        # Now you can call the file upload method with the path to your file
        self.upload_file(file_path, file_name)  # Example of uploading a file

        if sate_city_selection_method == "keyboard":
            self.select_state_and_city_using_keyboard(state, city)
        elif sate_city_selection_method == "selecting_option":
            self.select_state_and_city_using_css_selecting_option(state, city)


        self.select_state_and_city_using_xpath_selecting_option(state, city)  # Example of selecting state and city using the option clicking method


        # Finally, submit the form
        expect(self.submit_btn).to_be_visible()
        expect(self.submit_btn).to_be_enabled()
        self.submit_btn.click()  # Finally, submit the form