import requests
from pytest import mark


@mark.competition
class CompetitionsTests():
    """
    Test case for retrieving data related to competitions.

    This test suite includes tests for:
    1. Getting data for all competitions
    2. Getting data for a single competition
    3. Getting data for a single competition with invalid authorization
    4. Getting data for a single competition without authorization
    5. Getting standing data for a single competition
    """

    @mark.smoke
    def test_get_all_competitions_data(self, competition_uri, valid_token):
        """
        Test the retrieval of data for all competitions.

        Sends a GET request to the '/v4/competitions' endpoint and checks if
        the response status code is 200, indicating a successful request.
        """
        response = requests.get(competition_uri, headers=valid_token)
        print(response.text)
        assert response.status_code == 200

    def test_get_a_single_competition_data(self, competition_uri, valid_token, login_with_valid_token):
        """
        Test the retrieval of data for a single competition.

        Sends a GET request to the '/v4/competitions' endpoint with valid
        authorization cookies. Checks if the response status code is 200,
        indicating a successful request.
        """
        cookies = login_with_valid_token
        response = requests.get(competition_uri, headers=valid_token, cookies=cookies)
        print(response.text)
        assert response.status_code == 200

    def test_get_a_single_competition_data_with_an_invalid_token(self, competition_uri, invalid_token,
                                                                 login_with_invalid_token):
        """
        Test the retrieval of data for a single competition with invalid authorization.

        Sends a GET request to the '/v4/competitions' endpoint with invalid
        authorization cookies. Checks if the response status code is 403,
        indicating forbidden access.
        """
        cookies = login_with_invalid_token
        response = requests.get(competition_uri, headers=invalid_token, cookies=cookies)
        print(response.text)
        actual = response.json()
        expected = {
            "message": "Your API token is invalid.",
            "errorCode": 400
        }
        assert expected == actual

    def test_get_a_single_competition_data_without_a_token(self, competition_uri):
        """
        Test the retrieval of data for a single competition without authorization.

        Sends a GET request to the '/v4/competitions/BSA' endpoint without
        providing valid authorization. Checks if the response status code is 403,
        indicating forbidden access.
        """
        competition_code = "/BSA"
        uri = competition_uri + competition_code
        response = requests.get(uri)
        print(response.text)
        actual = response.json()
        expected = {
            "message": "The resource you are looking for is restricted and apparently not within your permissions. Please check your subscription.",
            "errorCode": 403
        }
        assert expected == actual

    def test_get_standing_data_for_single_competition(self, competition_uri, valid_token, login_with_valid_token):
        """
        Test the retrieval of standing data for a single competition.

        Sends a GET request to the '/v4/competitions/PL/standings' endpoint
        with valid authorization cookies. Checks if the response status code is 200,
        indicating a successful request.
        """
        standing_name = '/PL/standings'
        uri = competition_uri + standing_name
        cookies = login_with_valid_token
        response = requests.get(uri, headers=valid_token, cookies=cookies)
        print(response.text)
        assert response.status_code == 200