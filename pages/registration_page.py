from playwright.sync_api import Page, expect
import os
class RegistrationPage:
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

    def get_input(self, placeholder_text):
        return self.page.locator(self.DYNAMIC_FIELD_XPATH_INPUT.format(label=placeholder_text))

    def get_radio(self, value):
        return self.page.locator(self.DYNAMIC_FIELD_XPATH_RADIO.format(value=value))

    def get_checkbox(self, label):
        return self.page.locator(self.DYNAMIC_CHECKBOX_BY_LABEL.format(label=label))
    
    def get_dropdown_container(self, dropdown_id):
        return self.page.locator(self.DYNAMIC_DROPDOWN_CONTAINER.format(id_name=dropdown_id))

    def get_dropdown_option(self, option_text):
        return self.page.locator(self.DYNAMIC_DROPDOWN_OPTION.format(option_text=option_text))

    def get_date_input(self):
        return self.page.locator(self.DATE_INPUT)
    
    def get_date_select(self, type):
        return self.page.locator(self.DATE_SELECT_TEMPLATE.format(type=type))
    
    def get_day_locator(self, day):
        formatted_day = str(day).zfill(3)
        return self.page.locator(self.DAY_TEMPLATE.format(day=formatted_day))
    
    def navigate(self,url):
        # 1. Action: Navigate
        self.page.goto(url)

        # 2. Verification: Check the URL
        # We use 'expect' so Playwright waits for the URL to change
        expect(self.page).to_have_url(url)

        # 3. Verification: Check a Page Heading
        # This is the "Gold Standard" for verifying you are on the right page
        page_heading = self.page.locator("h1, .main-header")
        expect(page_heading).to_have_text("Practice Form")

        print("Success: Verified arrival at the Registration Form page.")


    def type_text(self, locator, value):
        """A robust action method that handles visibility, filling, and verification."""
        expect(locator).to_be_visible()
        expect(locator).to_be_enabled()
        locator.fill(value)
        return locator


    def check_hobby(self, hobby_name):
        locator = self.get_checkbox(hobby_name)
        expect(locator).to_be_visible()
        # On DemoQA, the input is often hidden; clicking the label sibling is safer
        # but since .check() works for you, we keep it robust:
        if not locator.is_checked():
            locator.check()
        return locator

    def select_gender(self, gender_name):
        locator = self.get_radio(gender_name)
        locator.check()
        return locator

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
        # 1. Open Calendar
        self.get_date_input().click()

        # 2. Select Month & Year
        # Note: We call .select_option() on the LOCATOR returned by our getter
        self.get_date_select("month").select_option(label=month)
        self.get_date_select("year").select_option(value=str(year))

        # 3. Select Day
        self.get_day_locator(day).click()


    def select_dropdown_by_type(self, dropdown_id, option_text):
        """Strategy: Opens the menu and uses keyboard simulation to select."""
        container = self.get_dropdown_container(dropdown_id)
        expect(container).to_be_visible()
        container.click()

        # We use the keyboard API for speed and to avoid scrolling issues
        self.page.keyboard.type(option_text)
        self.page.keyboard.press("Enter")

        return container  # Return the container for verification in the calling method
        
    def select_dropdown_by_click(self, dropdown_id, option_text):
        """Strategy: Opens the menu and clicks the specific text option."""
        container = self.get_dropdown_container(dropdown_id)
        expect(container).to_be_visible()
        container.click()

        option = self.get_dropdown_option(option_text)
        # React menus can have a slight 'fade-in' animation
        # This wait ensures the click actually registers
        option.wait_for(state="visible") 
        option.click()

        return container  # Return the container for verification in the calling method
        
    def upload_file(self, file_path, file_name):
        # 1. Ensure the file input is visible and enabled before interacting
        expect(self.file_picture_upload).to_be_visible()
        expect(self.file_picture_upload).to_be_enabled()
        # 1. Combine the folder path with the file name
        file_path = file_path + file_name

        # 2. Perform the upload 
        # REMINDER: Do not use .click() before this!
        self.file_picture_upload.set_input_files(file_path)

        return self.file_picture_upload  # Return the locator for verification in the calling method

        # # 3. Verification
        # actual_value = self.file_picture_upload.input_value()
        # assert file_name in actual_value
        # print(f"Verified: File '{file_name}' uploaded successfully from absolute path.")

    def fill_form(self, fname, lname, email, phone_num , gender=None, subjects=None, hobbies=[], address=None, day=None, month=None, year=None, file_path=None, file_name=None, state=None, city=None, use_keyboard=None):
      
        # We chain the 'type_text' action with our 'get_input' locator
        expect(self.type_text(self.get_input("First Name"), fname)).to_have_value(fname)
        
        expect(self.type_text(self.get_input("Last Name"), lname)).to_have_value(lname)

        expect(self.type_text(self.get_input("name@example.com"), email)).to_have_value(email)

        expect(self.type_text(self.get_input("Mobile Number"), phone_num)).to_have_value(phone_num)

        expect(self.select_gender( "Male" )).to_be_checked()
        expect(self.select_gender( "Other" )).to_be_checked()
        expect(self.select_gender( "Female" )).to_be_checked()
        expect(self.select_gender( gender )).to_be_checked()
        

        # This method takes a list of hobbies and checks the corresponding checkboxes
        # self.check_checkboxs(hobbies)  # Example of checking multiple checkboxes
        for hobby in hobbies:
            checkbox_locator = expect(self.get_checkbox(hobby)).to_be_visible()
            expect(self.check_hobby( hobby )).to_be_checked()

        # Subjects (Handles the auto-suggest input)
        expect(self.subjects_input).to_be_visible()
        self.subjects_input.fill(subjects)
        self.page.keyboard.press("Enter")
        expect(self.subjects_input).to_have_value("")  # After selection, the input should
        
        # Current Address (Handles textarea automatically!)
        expect(self.type_text(self.get_input("Current Address"), address)).to_have_value(address)

        # selecting date of birth using the method we defined
        self.select_dob(day, month, year)  # Example of selecting a date of birth
        # 4. Verify
        self.verify_date_ui(day, month, year)

        # Now you can call the file upload method with the path to your file
        result = self.upload_file(file_path, file_name)  # Example of uploading a file
        # Verification for file upload can be tricky since the input often just shows the file name or a fake path
        # You can verify that the file name is part of the input's value
        actual_value = result.input_value()
        assert file_name in actual_value, f"File upload failed! Expected '{file_name}' to be part of '{actual_value}'"
        print(f"Verified: File '{file_name}' uploaded successfully with value '{actual_value}'.")

        if use_keyboard:
            expect(self.select_dropdown_by_type("state", state)).to_contain_text(state)
            expect(self.select_dropdown_by_type("city", city)).to_contain_text(city)
        else:
            expect(self.select_dropdown_by_click("state", state)).to_contain_text(state)
            expect(self.select_dropdown_by_click("city", city)).to_contain_text(city)

        # Finally, submit the form
        expect(self.submit_btn).to_be_visible()
        expect(self.submit_btn).to_be_enabled()
        self.submit_btn.click()  # Finally, submit the form
        expect(self.page.locator("#example-modal-sizes-title-lg")).to_have_text("Thanks for submitting the form")
        print("Form submitted and confirmation modal verified successfully.")