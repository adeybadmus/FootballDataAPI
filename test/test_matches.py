import requests
from unittest import TestCase

from config import BASE_URL, HEADER


class MatchTest(TestCase):
    """
    Test case for retrieving match data.

    This test suite includes tests for:
    1. Getting match data for all competitions
    2. Getting match data for all competitions without a token
    3. Getting match data for all competitions with an invalid token
    4. Getting match data for a single team without a token
    5. Getting match data for a single team with an invalid token
    6. Getting match data for a single competition
    """

    def test_get_competitions_match_data(self):
        """
        Test the retrieval of match data for all competitions.

        This test sends a GET request to the '/v4/matches' endpoint with the provided
        header, and it checks if the response status code is 200, indicating a
        successful request.
        """
        base_url = BASE_URL
        resource = '/v4/matches'
        header = HEADER
        url = base_url + resource

        response = requests.get(url, headers=header)
        print(response.text)
        assert response.status_code == 200

    def test_get_competitions_match_data_without_a_token(self):
        """
        Test the retrieval of match data for all competitions without a token.

        This test sends a GET request to the '/v4/matches' endpoint without providing
        valid authorization. It checks if the response status code is 200, indicating
        successful access. Additionally, it asserts the response JSON structure.
        """
        base_url = BASE_URL
        resource = '/v4/matches'
        url = base_url + resource

        response = requests.get(url)
        print(response.text)
        assert response.status_code == 200

        actual = response.json()
        expected = {
            "filters": {
                "dateFrom": "2023-11-19",
                "dateTo": "2023-11-20",
                "permission": None
            },
            "resultSet": {
                "count": 0
            },
            "matches": []
        }

        assert expected == actual

    def test_get_competitions_match_data_with_an_invalid_token(self):
        """
        Test the retrieval of match data for all competitions with an invalid token.

        This test sends a GET request to the '/v4/matches' endpoint with an invalid
        header (token). It checks if the response status code is 400, indicating a
        bad request due to the invalid token.
        """
        base_url = BASE_URL
        resource = '/v4/matches'
        invalid_token = {'Authorization': 'Bearer 556TGHHYUUY77'}
        url = base_url + resource

        response = requests.get(url, headers=invalid_token)
        actual = response.json()

        expected = {
            "message": "Your API token is invalid.",
            "errorCode": 400
        }
        assert expected == actual

    def test_get_match_data_for_a_single_team_without_a_token(self):
        """
        Test the retrieval of match data for a single team without a token.

        This test sends a GET request to the '/v4/teams/759/matches' endpoint without
        providing valid authorization. It checks if the response status code is 403,
        indicating forbidden access.
        """
        base_url = BASE_URL
        resource = '/v4/teams/759/matches'
        url = base_url + resource

        response = requests.get(url)
        actual = response.json()

        expected = {
            "message": "The resource you are looking for is restricted and apparently not within your permissions. Please check your subscription.",
            "errorCode": 403
        }
        assert expected == actual

    def test_get_match_data_for_a_single_team_with_an_invalid_token(self):
        """
        Test the retrieval of match data for a single team with an invalid token.

        This test sends a GET request to the '/v4/teams/759/matches' endpoint with an
        invalid header (token). It checks if the response status code is 400, indicating
        a bad request due to the invalid token.
        """
        base_url = BASE_URL
        resource = '/v4/teams/759/matches'
        invalid_token = {'Authorization': 'Bearer 56TGHHYUU7'}
        url = base_url + resource

        response = requests.get(url, headers=invalid_token)
        actual = response.json()

        expected = {
            "message": "Your API token is invalid.",
            "errorCode": 400
        }
        assert expected == actual

    def test_get_a_single_competitions_match_data(self):
        """
        Test the retrieval of match data for a single competition.

        This test sends a GET request to the '/v4/competitions/CL/matches' endpoint with
        the provided header, and it checks if the response status code is 200, indicating
        a successful request.
        """
        base_url = BASE_URL
        resource = '/v4/competitions/CL/matches'
        header = HEADER
        url = base_url + resource

        response = requests.get(url, headers=header)
        print(response.text)
        assert response.status_code == 200
