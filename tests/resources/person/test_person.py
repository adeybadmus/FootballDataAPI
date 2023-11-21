import requests
from pytest import mark


@mark.person
class PersonTests():
    """
    Test case for retrieving person data.

    This test suite includes tests for:
    1. Getting person data with valid authorization
    2. Getting person data without a token
    3. Getting person data with an invalid token
    """

    def test_get_person_data_with_valid_authorization(self, person_uri, valid_token):
        """
        Test the retrieval of person data with valid authorization.

        This test makes a GET request to the '/v4/persons/44' endpoint with valid
        authorization cookies. It then compares the response with the expected data.
        """
        # Set up the request parameters
        uri = f"{person_uri}/44"

        # Login to obtain cookies
        cookies = login()

        response = requests.get(uri, headers=valid_token, cookies=cookies)
        actual = response.json()
        expected_name = "Cristiano"
        expected_position = "Offence"
        assert actual["name"] == expected_name
        assert actual["position"] == expected_position


    @mark.smoke
    def test_get_person_data_with_valid_authorization_extended(self, person_uri, valid_token):
        """
        Test the retrieval of person data with valid authorization (extended).

        This test makes a GET request to the '/v4/persons/44' endpoint with valid
        authorization cookies. It then compares the response with the expected data,
        including detailed information about the person.
        """
        # Set up the request parameters
        uri = f"{person_uri}/44"

        # Login to obtain cookies
        cookies = login()

        response = requests.get(uri, headers=valid_token, cookies=cookies)
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


    def test_get_person_data_without_a_token(self, person_uri):
        """
        Test the retrieval of person data without a token.

        This test makes a GET request to the '/v4/persons/44' endpoint without
        providing valid authorization. It then compares the response with the
        expected data.
        """
        # Set up the request parameters
        uri = f"{person_uri}/44"

        response = requests.get(uri)
        actual = response.json()

        expected = {
            "message": "The resource you are looking for is restricted and apparently not within your permissions. Please check your subscription.",
            "errorCode": 403
        }

        assert expected == actual


    def test_get_person_data_with_an_invalid_token(self, person_uri, invalid_token):
        """
        Test the retrieval of person data with an invalid token.

        This test makes a GET request to the '/v4/persons/44' endpoint with an
        invalid header (token). It then compares the response with the expected data.
        """
        # Set up the request parameters
        uri = f"{person_uri}/44"
        response = requests.get(uri, headers=invalid_token)
        actual = response.json()

        expected = {
            "message": "Your API token is invalid.",
            "errorCode": 400
        }

        assert expected == actual
