from unittest.mock import patch, MagicMock

API_BASE_URL = "https://bobsburgers-api.herokuapp.com"   

MOCK_BOB_RESPONS = {
    "id": 491,
    "gender": "Male",
    "hair": "Black",
    "allOccupations": [
        "Chef/owner & operator of Bob's Burgers",
        "Chaperone/volunteer for Wagstaff School",
        "Student at Buchannan Middle School (formerly)",
        "Grill cook/server/busser at Big Bob's Diner (formerly) (briefly)",
        "Cab driver (briefly)",
        "Guest chef for the Windbreaker (forcibly, formerly)",
        "Fraternity chef (briefly)",
        "Home economics substitute teacher for Wagstaff School (formerly)",
        "Member of the North Atlantic Burger Lovers",
        "Coach for the Gold Dragons (forcibly, briefly)",
        "Cook for Patricia's 77 Sandwiches (briefly)",
        "Limousine driver (briefly)"
    ],
    "relatives": [
    {
      "name": "Big Bob",
      "relationship": "father",
      "wikiUrl": "https://bobs-burgers.fandom.com/wiki/Big_Bob",
      "url": "https://bobsburgers-api.herokuapp.com/characters/490"
    },
    {
      "name": "Lily Belcher",
      "relationship": "mother",
      "wikiUrl": "https://bobs-burgers.fandom.com/wiki/Lily_Belcher",
      "url": "https://bobsburgers-api.herokuapp.com/characters/319"
    },
    {
      "name": "Al Genarro",
      "relationship": "father-in-law",
      "wikiUrl": "https://bobs-burgers.fandom.com/wiki/Al_Genarro",
      "url": "https://bobsburgers-api.herokuapp.com/characters/6"
    },
    {
      "name": "Gloria Genarro",
      "relationship": "mother-in-law",
      "wikiUrl": "https://bobs-burgers.fandom.com/wiki/Gloria_Genarro",
      "url": "https://bobsburgers-api.herokuapp.com/characters/208"
    },
    {
      "name": "Gayle Genarro",
      "relationship": "sister-in-law",
      "wikiUrl": "https://bobs-burgers.fandom.com/wiki/Gayle_Genarro",
      "url": "https://bobsburgers-api.herokuapp.com/characters/195"
    },
    {
      "name": "Ernest Lombard",
      "relationship": "maternal uncle",
      "wikiUrl": "https://bobs-burgers.fandom.com/wiki/Ernest_Lombard",
      "url": "https://bobsburgers-api.herokuapp.com/characters/173"
    },
    {
      "name": "Alice Lombard",
      "relationship": "maternal grandmother",
      "wikiUrl": "https://bobs-burgers.fandom.com/wiki/Alice_Lombard",
      "url": "https://bobsburgers-api.herokuapp.com/characters/12"
    },
    {
      "name": "Billy Lombard",
      "relationship": "maternal grandfather",
      "wikiUrl": "https://bobs-burgers.fandom.com/wiki/Billy_Lombard",
      "url": "https://bobsburgers-api.herokuapp.com/characters/55"
    },
    {
      "name": "Gertie",
      "relationship": "maternal great-grandmother",
      "wikiUrl": "https://bobs-burgers.fandom.com/wiki/Gertie",
      "url": "https://bobsburgers-api.herokuapp.com/characters/199"
    },
    {
      "name": "Burt Rinaldi",
      "relationship": "grandfather-in-law",
      "wikiUrl": "https://bobs-burgers.fandom.com/wiki/Burt_Rinaldi",
      "url": "https://bobsburgers-api.herokuapp.com/characters/67"
    },
    {
      "name": "Vanessa",
      "relationship": "cousin",
      "wikiUrl": "https://bobs-burgers.fandom.com/wiki/Cousin_Vanessa",
      "url": None
    },
    {
      "name": "Marie",
      "relationship": "cousin-in-law",
      "wikiUrl": "https://bobs-burgers.fandom.com/wiki/Marie",
      "url": None
    }
    ],
    "occupation": "Chef/owner & operator of Bob's Burgers",
    "voicedBy": "H. Jon Benjamin"
}

def mock_character_get(url, **kwargs):
    mock = MagicMock()
    if url == f"{API_BASE_URL}/characters/491":
        mock.status_code = 200
        mock.json.return_value = MOCK_BOB_RESPONS
    else:
        mock.status_code = 500
        mock.json.return_value = {"error": "Error while retreiving data with id 9999"}
    return mock


def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")

    if "regression" in scenario.tags:
        context.mock_get = patch("requests.get", side_effect=mock_character_get)
        context.mock_get.start()


def after_scenario(context, scenario):
    print( f"Finished scenario: " f"{scenario.name} - Status: {scenario.status}")

    if "regression" in scenario.tags:
        context.mock_get.stop() 