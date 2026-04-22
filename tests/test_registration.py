import pytest
from pages.registration_page import RegistrationPage
from utils.data_generator import DataGenerator # New Import


# This decorator tells pytest to run this function 2 times
# We use "_" because we don't actually need to use the number inside the test
@pytest.mark.parametrize("iteration", range(1))
def test_full_registration(page, iteration):
    # 1. Initialize Objects
    data_gen = DataGenerator()
    
    # 2. Get the generated data dictionary
    # Every time the loop runs, get_registration_data() generates NEW random values
    test_data = data_gen.get_registration_data()

    # 3. Navigate
    url = "https://demoqa.com/automation-practice-form"
    # reg_page.navigate(url)
    RegistrationPage.navigate(page,url)

    
    # 4. Fill the form using Dictionary Unpacking (**)
    # This sends all dictionary values to the matching parameters in fill_form
    RegistrationPage.fill_form(page, **test_data)

    # print(f"Completed iteration {iteration + 1} with user: {test_data['fname']}")

    # page.wait_for_timeout(3000)