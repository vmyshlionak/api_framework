def test_created_pet(pet_endpoint1):
    pet_endpoint1.get_response_when_create_pet()
    pet_endpoint1.check_pets_price()
    pet_endpoint1.check_pets_microchipped()
    pet_endpoint1.check_len_pet_id()
    pet_endpoint1.check_response_status_code_ok()


