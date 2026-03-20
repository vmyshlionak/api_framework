import requests
from endpoints.endpoints_handler import Endpoint


class GetPetsEndpoint(Endpoint):
    pets_endpoint = None
    species = None
    len_id = None
    len_name = None
    items_quantity = None

    def get_response_when_get_pets_endpoint(self, pet_id=None):
        if pet_id:
            self.pets_endpoint = f'https://api.petstoreapi.com/v1/pets/{pet_id}'
        else:
            self.pets_endpoint = 'https://api.petstoreapi.com/v1/pets'

        response = requests.get(self.pets_endpoint)
        self.status = response.status_code
        if pet_id:
          self.species = response.json()['species']
          self.len_id = len(response.json()['id'])
          self.items_quantity = None
        else:
          self.species = None
          self.len_id = None
          self.items_quantity = response.json()['pagination']['totalItems']


    def check_pets_species(self):
        assert self.species == 'DOG'

    def check_pets_len_id(self):
        assert self.len_id > 0

    def count_items_when_get_pets_endpoint(self):
        assert self.items_quantity > 1800