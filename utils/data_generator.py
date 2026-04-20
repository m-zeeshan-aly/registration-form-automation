import random
from faker import Faker
import os

class DataGenerator:
    def __init__(self):
        self.fake = Faker()
        
        # 1. Define the State-City Relationship
        self.location_map = {
            "NCR": ["Delhi", "Gurgaon", "Noida"],
            "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
            "Haryana": ["Karnal", "Panipat"],
            "Rajasthan": ["Jaipur", "Jaiselmer"]
        }

    def get_registration_data(self):
        # 2. Pick a random State from the keys
        random_state = random.choice(list(self.location_map.keys()))
        
        # 3. Pick a random City from that specific State's list
        random_city = random.choice(self.location_map[random_state])

        # 4. Generate a random Date of Birth
        # We generate a date, then extract day, month, year as strings
        random_dob = self.fake.date_of_birth(minimum_age=18, maximum_age=60)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        file_path = os.path.join(project_root, "file_upload")

        return {
            "fname": self.fake.first_name(),
            "lname": self.fake.last_name(),
            "email": self.fake.ascii_free_email(),
            "phone_num": self.fake.msisdn()[:10],
            "gender": random.choice(["male", "female", "other"]),
            "subjects": "Maths",
            "hobbies": ["Sports", "Music"],
            "address": self.fake.address().replace("\n", ", "),
            # 5. Format the Date for your POM method
            "day": str(random_dob.day),
            "month": random_dob.strftime("%B"), # Full month name like 'January'
            "year": str(random_dob.year),
            "file_path": file_path + "/",
            "file_name": "file_upload_example.jpeg",
            "state": random_state,
            "city": random_city,
            "sate_city_selection_method": random.choice(["keyboard", "selecting_option"])  # Randomly choose a method for selecting state and city
        }