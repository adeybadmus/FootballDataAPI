import requests
from pytest import mark

@mark.matches
class MatchTests():
    """
    Test case for retrieving match data.

    This tests suite includes tests for:
    1. Getting match data for all competitions
    2. Getting match data for all competitions without a token
    3. Getting match data for all competitions with an invalid token
    4. Getting match data for a single team without a token
    5. Getting match data for a single team with an invalid token
    6. Getting match data for a single competition
    """

    def test_get_match_data_for_a_competition(self, match_uri, valid_token):
        """
        Test the retrieval of match data for all competitions.

        This tests sends a GET request to the '/v4/matches' endpoint with the provided
        header, and it checks if the response status code is 200, indicating a
        successful request.
        """

        response = requests.get(match_uri, valid_token)
        print(response.text)
        assert response.status_code == 200

    def test_get_match_data_for_a_competition_without_a_token(self,  match_uri):
        """
        Test the retrieval of match data for all competitions without a token.

        This tests sends a GET request to the '/v4/matches' endpoint without providing
        valid authorization. It checks if the response status code is 200, indicating
        successful access. Additionally, it asserts the response JSON structure.
        """

        response = requests.get(match_uri)
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

    def test_gets_match_data_for_a_competition_with_an_invalid_token(self, match_uri, invalid_token):
        """
        Test the retrieval of match data for all competitions with an invalid token.

        This tests sends a GET request to the '/v4/matches' endpoint with an invalid
        header (token). It checks if the response status code is 400, indicating a
        bad request due to the invalid token.
        """

        response = requests.get(match_uri, headers=invalid_token)
        actual = response.json()

        expected = {
            "message": "Your API token is invalid.",
            "errorCode": 400
        }
        assert expected == actual

    def test_get_match_data_for_a_single_team_without_a_token(self, match_uri):
        """
        Test the retrieval of match data for a single team without a token.

        This tests sends a GET request to the '/v4/teams/759/matches' endpoint without
        providing valid authorization. It checks if the response status code is 403,
        indicating forbidden access.
        """

        response = requests.get(match_uri)
        actual = response.json()

        expected = {
            "message": "The resource you are looking for is restricted and apparently not within your permissions. Please check your subscription.",
            "errorCode": 403
        }
        assert expected == actual

    def test_get_match_data_for_a_single_team_with_an_invalid_token(self, match_uri, invalid_token):
        """
        Test the retrieval of match data for a single team with an invalid token.

        This tests sends a GET request to the '/v4/teams/759/matches' endpoint with an
        invalid header (token). It checks if the response status code is 400, indicating
        a bad request due to the invalid token.
        """

        response = requests.get(match_uri, headers=invalid_token)
        actual = response.json()

        expected = {
            "message": "Your API token is invalid.",
            "errorCode": 400
        }
        assert expected == actual

    def test_get_a_single_competitions_match_data(self, match_uri, valid_token):
        """
        Test the retrieval of match data for a single competition.

        This tests sends a GET request to the '/v4/competitions/CL/matches' endpoint with
        the provided header, and it checks if the response status code is 200, indicating
        a successful request.
        """

        response = requests.get(match_uri, headers=valid_token)
        print(response.text)
        assert response.status_code == 200
