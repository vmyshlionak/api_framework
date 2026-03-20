import pytest
import requests
import allure_pytest
from endpoints.get_pets_enpoint import GetPetsEndpoint
from endpoints.create_pet_endpoint import CreatePetEndpoint

@pytest.fixture()
def pet_endpoint():
    endpoint = GetPetsEndpoint()
    return endpoint

@pytest.fixture()
def pet_endpoint1():
    endpoint = CreatePetEndpoint()
    return endpoint

@pytest.fixture()
def new_pet_id():
    body = {
        "name": "Isabella",
        "species": "DOG",
        "breed": "Chihuahua",
        "ageMonths": 18,
        "size": "SMALL",
        "color": "Golden",
        "goodWithKids": False,
        "price": "5000.00",
        "currency": "USD",
        "status": "AVAILABLE",
        "description": "Pure evil is looking for its victims",
        "medicalInfo": {
            "spayedNeutered": True,
            "microchipped": True,
            "specialNeeds": False,
            "healthNotes": "Up to date on all vaccinations"
        }
    }
    headers = {'Authorization': 'Bearer {{bearerToken}}'}
    response = requests.post('https://api.petstoreapi.com/v1/pets', json=body, headers=headers).json()
    pet_id = response['id']
    print(pet_id)
    yield pet_id
    print('\ndeleting pet')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{pet_id}')