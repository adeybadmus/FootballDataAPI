import requests
from unittest import TestCase

from config import HEADER, BASE_URL
from login import login, invalid_login


class CompetitionsTest(TestCase):
    """
    Test case for retrieving data related to competitions.

    This test suite includes tests for:
    1. Getting data for all competitions
    2. Getting data for a single competition
    3. Getting data for a single competition with invalid authorization
    4. Getting data for a single competition without authorization
    5. Getting standing data for a single competition
    """

    def test_get_all_competitions_data(self):
        """
        Test the retrieval of data for all competitions.

        This test sends a GET request to the '/v4/competitions' endpoint and checks if
        the response status code is 200, indicating a successful request.
        """
        header = HEADER
        base_url = BASE_URL
        resource = "/v4/competitions"
        url = base_url + resource
        response = requests.get(url, headers=header)
        print(response.text)
        assert response.status_code == 200

    def test_get_a_single_competition_data(self):
        """
        Test the retrieval of data for a single competition.

        This test sends a GET request to the '/v4/competitions' endpoint with valid
        authorization cookies. It checks if the response status code is 200,
        indicating a successful request.
        """
        header = HEADER
        base_url = BASE_URL
        resource = '/v4/competitions'
        url = base_url + resource

        cookies = login()

        response = requests.get(url, headers=header, cookies=cookies)

        print(response.text)
        assert response.status_code == 200

    def test_get_a_single_competition_data_with_an_invalid_token(self):
        """
        Test the retrieval of data for a single competition with invalid authorization.

        This test sends a GET request to the '/v4/competitions' endpoint with invalid
        authorization cookies. It checks if the response status code is 403,
        indicating forbidden access.
        """
        invalid_token = {'X-Auth-Token': '55673hhjjjjkjkdd'}
        base_url = BASE_URL
        resource = '/v4/competitions'
        url = base_url + resource

        cookies = invalid_login()

        response = requests.get(url, headers=invalid_token, cookies=cookies)

        print(response.text)
        actual = response.json()

        expected = {
            "message": "Your API token is invalid.",
            "errorCode": 400
        }
        assert expected == actual

    def test_get_a_single_competition_data_without_a_token(self):
        """
        Test the retrieval of data for a single competition without authorization.

        This test sends a GET request to the '/v4/competitions/BSA' endpoint without
        providing valid authorization. It checks if the response status code is 403,
        indicating forbidden access.
        """
        base_url = BASE_URL
        resource = "/v4/competitions/BSA"
        url = base_url + resource
        response = requests.get(url)
        print(response.text)
        actual = response.json()

        expected = {
            "message": "The resource you are looking for is restricted and apparently not within your permissions. Please check your subscription.",
            "errorCode": 403
        }
        assert expected == actual

    def test_get_standing_data_for_single_competition(self):
        """
        Test the retrieval of standing data for a single competition.

        This test sends a GET request to the '/v4/competitions/PL/standings' endpoint
        with valid authorization cookies. It checks if the response status code is 200,
        indicating a successful request.
        """
        header = HEADER
        base_url = BASE_URL
        resource = '/v4/competitions/PL/standings'
        url = base_url + resource

        cookies = login()

        response = requests.get(url, headers=header, cookies=cookies)

        print(response.text)
        assert response.status_code == 200
