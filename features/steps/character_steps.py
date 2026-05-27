from behave import given, when, then
import requests

API_BASE_URL = "https://bobsburgers-api.herokuapp.com"


@given("the Bob's Burgers API is available")
def step_given_api_available(context):
    response=requests.get(f"{API_BASE_URL}/characters/491")
    assert response.status_code == 200

@when("I request the character with ID {character_id:d}")
def step_request_character_ID(context, character_id):
    context.response=requests.get(f"{API_BASE_URL}/characters/{character_id}")

@then("the response status code should be {expected_status:d}")
def step_response_status_code(context, expected_status):
    assert context.response.status_code == expected_status

@then("the basic fields should match:")
def step_basic_fields_should_match(context):
    data = context.response.json()
    for row in context.table:
        field = row["fields"]
        expected = row["values"]
        actual_value = data.get(field)
        print(f"Field: {field}, Expected: '{expected}', Actual: '{actual_value}'")
        assert str(actual_value) == str(expected), f"Expected '{expected}' but got '{actual_value}'"


@then('the allOccupations should contain "{expected_occupation}"')
def step_then_all_occupations(context, expected_occupation):
    data = context.response.json()
    assert expected_occupation in data["allOccupations"]

@then("the character has more than five relatives")
def step_then_relatives(context):
    data = context.response.json()
    assert len(data["relatives"]) > 5, (
        f"Expected more than 5 relatives but got {len(data['relatives'])}"
    )    

@then('the voicedBy is "{expected_voice}"')
def step_then_voiced_by(context, expected_voice):
    data = context.response.json()
    assert data["voicedBy"] == expected_voice

@then("the response should contain an error message")
def step_then_error_message(context):
    data = context.response.json()
    assert "error" in data




