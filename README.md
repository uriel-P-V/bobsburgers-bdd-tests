# bobsburgers-bdd-tests

![CI](https://github.com/uriel-P-V/bobsburgers-bdd-tests/actions/workflows/tests.yml/badge.svg)

A BDD-based test suite for the Bob's Burgers API —
demonstrates deep contract validation with Behave and Gherkin,
testing list membership, relative count validation,
and non-standard error responses (500 instead of 404).

---

## Project Structure

```
bobsburgers-bdd-tests/
├── .github/
│   └── workflows/
│       └── tests.yml              ← GitHub Actions CI
├── features/
│   ├── steps/
│   │   └── character_steps.py     ← All step definitions
│   ├── environment.py             ← Hooks and mock setup
│   └── character.feature          ← 6 deep BDD scenarios
└── requirements.txt
```

---

## Features

- **List membership validation** — verifies occupation exists in `allOccupations` list
- **Relative count validation** — verifies character has more than 5 relatives
- **Voice actor validation** — validates `voicedBy` field contract
- **Non-standard error handling** — API returns 500 instead of 404 for invalid IDs
- **Single mock** — one `patch("requests.get")` with URL discrimination
- **Tag-driven execution** — `@smoke` hits real API, `@regression` fully mocked
- **GitHub Actions CI** — smoke runs first, regression only if smoke passes

---

## BDD Scenarios

```gherkin
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
      | fields     | values                                 |
      | id         | 491                                    |
      | gender     | Male                                   |
      | hair       | Black                                  |
      | occupation | Chef/owner & operator of Bob's Burgers |

  @regression
  Scenario: Validate that allOccupations contains main occupation
    When I request the character with ID 491
    Then the allOccupations should contain "Chef/owner & operator of Bob's Burgers"

  @regression
  Scenario: invalid character
    When I request the character with ID 9999
    Then the response status code should be 500
    And the response should contain an error message
```

---

## Mock Strategy

Single `patch("requests.get")` with URL discrimination —
returns Bob Belcher mock data for valid requests, 500 with error JSON for anything else.

```python
def mock_character_get(url, **kwargs):
    mock = MagicMock()
    if url == f"{API_BASE_URL}/characters/491":
        mock.status_code = 200
        mock.json.return_value = MOCK_BOB_RESPONSE
    else:
        mock.status_code = 500
        mock.json.return_value = {"error": "Error while retreiving data with id 9999"}
    return mock
```

> **Note:** This API returns 500 instead of the standard 404 for invalid IDs —
> a known API design issue documented in [BUG-007](https://github.com/uriel-P-V/qa-portfolio).

---

## Setup

```bash
git clone https://github.com/uriel-P-V/bobsburgers-bdd-tests.git
cd bobsburgers-bdd-tests
pip install -r requirements.txt
behave
```

---

## Running Tests

```bash
# All scenarios
behave

# Smoke only — hits real Bob's Burgers API
behave --tags=smoke

# Regression only — fully mocked, no internet required
behave --tags=regression
```

---

## CI/CD Pipeline

Two dependent jobs run on every push and pull request to `main`:

```
push / PR → smoke (1 scenario) → regression (5 scenarios)
```

If `smoke` fails, `regression` is skipped automatically.

---

## Tech Stack

- **Python 3.11+**
- **Behave** — BDD framework with Gherkin support
- **Requests** — HTTP client for API calls
- **unittest.mock** — patch, MagicMock, side_effect
- **GitHub Actions** — CI/CD pipeline

---

## Author

**Uriel Alejandro Pérez Valdovinos**  
[github.com/uriel-P-V](https://github.com/uriel-P-V) · [linkedin.com/in/uriel-pv](https://linkedin.com/in/uriel-pv)