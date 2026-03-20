import requests
from endpoints.endpoints_handler import Endpoint


class CreatePetEndpoint(Endpoint):
    pets_endpoint = None
    pet_id = None
    pet_price = None
    pet_microchipped = None
    body = None
    headers = None


    def get_response_when_create_pet(self):
        self.pets_endpoint = 'https://api.petstoreapi.com/v1/pets'
        self.body = {
            "name": "Max",
            "species": "DOG",
            "breed": "Golden Retriever",
            "ageMonths": 24,
            "size": "LARGE",
            "color": "Golden",
            "gender": "MALE",
            "goodWithKids": True,
            "price": "250.00",
            "currency": "USD",
            "status": "AVAILABLE",
            "description": "Friendly golden retriever looking for an active family",
            "medicalInfo": {
                "vaccinated": True,
                "spayedNeutered": True,
                "microchipped": True,
                "specialNeeds": False,
                "healthNotes": "Up to date on all vaccinations"
            }
        }


        self.headers = {'Authorization': 'Bearer {{bearerToken}}'}
        response = requests.post(self.pets_endpoint, json=self.body, headers=self.headers)
        print(response.json())
        self.status = response.status_code
        self.pet_id = response.json()['id']
        self.pet_price = response.json()['price']
        self.pet_microchipped = response.json()['medicalInfo']['microchipped']

        # return self.pet_id, self.pet_price, self.pet_microchipped


    def check_pets_price(self):
        assert self.pet_price == '250.00'


    def check_pets_microchipped(self):
        assert self.pet_microchipped == True

    def check_len_pet_id(self):
        assert len(self.pet_id) == 36
