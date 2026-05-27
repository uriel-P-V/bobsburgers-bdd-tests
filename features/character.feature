Feature: Bob's Burgers API

  Background:
    Given the Bob's Burgers API is available 

  @smoke
  Scenario: Get Bob Belcher by ID
    When I request the character with ID 491 
    Then the response status code should be 200

  @regression
  Scenario: Validate basic fields with table
    When I request the character with ID 491
    Then the basic fields should match:
        |fields      |values                                 |
        |id          |491                                    |
        |gender      |Male                                   |
        |hair        |Black                                  |
        |occupation  |Chef/owner & operator of Bob's Burgers |
        
  @regression
  Scenario: Validate that allOccupations contains main occupation
    When I request the character with ID 491
    Then the allOccupations should contain "Chef/owner & operator of Bob's Burgers"

  @regression
  Scenario: Validate that you have more than 5 relatives
    When I request the character with ID 491
    Then the character has more than five relatives 

  @regression
  Scenario: Validate that voicedBy
    When I request the character with ID 491
    Then the voicedBy is "H. Jon Benjamin"

  @regression
  Scenario: invalid character
    When I request the character with ID 9999
    Then the response status code should be 500
    And the response should contain an error message



