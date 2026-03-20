def test_get_a_pet(pet_endpoint, new_pet_id):
    pet_endpoint.get_response_when_get_pets_endpoint(new_pet_id)
    pet_endpoint.check_response_status_code_ok()
    pet_endpoint.check_pets_species()
    pet_endpoint.check_pets_len_id()

def test_get_all_pets(pet_endpoint):
    pet_endpoint.get_response_when_get_pets_endpoint()
    pet_endpoint.check_response_status_code_ok()
    pet_endpoint.count_items_when_get_pets_endpoint()




