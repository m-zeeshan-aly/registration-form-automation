from pages.registration_page import RegistrationPage
def test_full_registration(page):

    # 1. Initialize the RegistrationPage object
    reg_page = RegistrationPage(page)

    # 2. Navigate to the registration form
    reg_page.navigate()

    # 3. Call your method
    first_name = "Muhammad"
    last_name = "Zeeshan"
    email = "zeeshan@example.com"
    phone = "0320840239"
    gender = "male"
    subjects = "Maths, Physics"
    hobbies = ["Sports", "Reading"]
    address = "123 Main St, Anytown"

    day = "9"
    month = "January"
    year = "1970"

    file_path = "/home/ibraheem/Music/vfairs/registrationFormPlaywright/file_upload/"  # Update this path to your actual picture file
    file_name = "file_upload_example.jpeg"  # The name of the file to be uploaded

    state = "Uttar Pradesh"
    city = "Lucknow"
    reg_page.fill_form(first_name, last_name, email, phone, gender, subjects, hobbies, address ,day , month, year, file_path, file_name, state, city)
    page.wait_for_timeout(10000)  # Wait for 5 seconds to observe the filled form (optional)
