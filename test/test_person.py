import requests
from unittest import TestCase

from config import BASE_URL, HEADER
from login import login


class PersonTest(TestCase):
    """
    Test case for retrieving person data.

    This test suite includes tests for:
    1. Getting person data with valid authorization
    2. Getting person data without a token
    3. Getting person data with an invalid token
    """

    def test_get_person_data(self):
        """
        Test the retrieval of person data with valid authorization.

        This test makes a GET request to the '/v4/persons/44' endpoint with valid
        authorization cookies. It then compares the response with the expected data.
        """
        # Set up the request parameters
        base_url = BASE_URL
        resource = '/v4/persons/44'
        header = HEADER
        url = base_url + resource

        # Login to obtain cookies
        cookies = login()

        response = requests.get(url, headers=header, cookies=cookies)
        actual = response.json()

        expected = {
            "id": 44,
            "name": "Cristiano Ronaldo",
            "firstName": "",
            "lastName": "Cristiano Ronaldo",
            "dateOfBirth": "1985-02-05",
            "nationality": "Portugal",
            "section": "Offence",
            "position": "Offence",
            "shirtNumber": 7,
            "lastUpdated": "2023-09-19T09:52:08Z",
            "currentTeam": {
                "area": {
                    "id": 2187,
                    "name": "Portugal",
                    "code": "POR",
                    "flag": "https://crests.football-data.org/765.svg"
                },
                "id": 765,
                "name": "Portugal",
                "shortName": "Portugal",
                "tla": "POR",
                "crest": "https://crests.football-data.org/765.svg",
                "address": "Rua Alexandre Herculano, 58 Lisboa 1250-012",
                "website": "http://www.fpf.pt",
                "founded": 1914,
                "clubColors": "Red / Green",
                "venue": "Estádio José Alvalade",
                "runningCompetitions": [
                    {
                        "id": 2165,
                        "name": "European Championship Qualifiers",
                        "code": "ECQ",
                        "type": "CUP",
                        "emblem": None
                    }
                ],
                "contract": {
                    "start": None,
                    "until": None
                }
            }
        }

        assert expected == actual

    def test_get_person_data_without_a_token(self):
        """
        Test the retrieval of person data without a token.

        This test makes a GET request to the '/v4/persons/44' endpoint without
        providing valid authorization. It then compares the response with the
        expected data.
        """
        # Set up the request parameters
        base_url = BASE_URL
        resource = '/v4/persons/44'
        url = base_url + resource

        response = requests.get(url)
        actual = response.json()

        expected = {
            "message": "The resource you are looking for is restricted and apparently not within your permissions. Please check your subscription.",
            "errorCode": 403
        }

        assert expected == actual

    def test_get_person_data_with_an_invalid_token(self):
        """
        Test the retrieval of person data with an invalid token.

        This test makes a GET request to the '/v4/persons/44' endpoint with an
        invalid header (token). It then compares the response with the expected data.
        """
        # Set up the request parameters
        base_url = BASE_URL
        resource = '/v4/persons/44'
        url = base_url + resource
        invalid_token = {'X-Auth-Token': '55673hhjjjjkjkdd'}

        response = requests.get(url, headers=invalid_token)
        actual = response.json()

        expected = {
            "message": "Your API token is invalid.",
            "errorCode": 400
        }

        assert expected == actual
