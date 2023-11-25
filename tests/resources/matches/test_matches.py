import requests
from pytest import mark

@mark.matches
class MatchTests:
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

    def test_get_match_across_a_set_of_competition_with_a_valid_token(self, match_uri, valid_token, login_with_valid_token):
        """
        Test the retrieval of match data for all competitions.

        Sends a GET request to the '/v4/matches' endpoint with the provided
        header, and it checks if the response status code is 200, indicating a
        successful request.

        Args:
            match_uri (str): The base URI for the matches resource.
            valid_token (dict): Valid authentication token.

        Returns:
            None
        """
        cookies = login_with_valid_token
        response = requests.get(match_uri, headers=valid_token, cookies=cookies)
        assert response.status_code == 200
        actual = response.json()
        assert actual["resultSet"]["competitions"] == "BSA,PL,PD,SA,BL1,ELC,DED,FL1"
        assert actual["matches"][0]["competition"]["code"] == "BSA"
        assert actual["matches"][1]["competition"]["code"] == "PL"
        assert actual["matches"][2]["competition"]["code"] == "PD"
        assert actual["matches"][3]["competition"]["code"] == "SA"
        assert actual["matches"][4]["competition"]["code"] == "BL1"
        assert actual["matches"][5]["competition"]["code"] == "ELC"
        assert actual["matches"][6]["competition"]["code"] == "DED"
        assert actual["matches"][7]["competition"]["code"] == "FL1"

    @mark.mar
    def test_get_match_data_for_a_competition_without_a_token(self,  match_uri):
        """
        Test the retrieval of match data for all competitions without a token.

        Sends a GET request to the '/v4/matches' endpoint without providing
        valid authorization. Checks if the response status code is 200, indicating
        successful access. Additionally, it asserts the response JSON structure.

        Args:
            match_uri (str): The base URI for the matches resource.

        Returns:
            None
        """

        response = requests.get(match_uri)
        assert response.status_code == 200

        actual = response.json()

        assert actual["resultSet"]["count"] == 0
        assert actual["matches"] == []

    def test_gets_match_data_for_a_competition_with_an_invalid_token(self, competition_uri, invalid_token):
        """
        Test the retrieval of match data for all competitions with an invalid token.

        Sends a GET request to the 'competitions/2003/matches?matchday=1' endpoint with an invalid
        header (token). Checks if the response status code is 400, indicating a
        bad request due to the invalid token.

        Args:
            match_uri (str): The base URI for the matches resource.
            invalid_token (dict): Invalid authentication token.

        Returns:
            None
        """
        uri = f"{competition_uri}/2003/matches?matchday=1"
        response = requests.get(uri, headers=invalid_token)
        actual = response.json()

        expected = {
            "message": "Your API token is invalid.",
            "errorCode": 400
        }
        assert expected == actual

    def test_get_match_data_for_a_particluar_team_without_a_token(self, base_uri):
        """
        Test the retrieval of match data for a single team without a token.

        Sends a GET request to the '/v4/teams/759/matches' endpoint without
        providing valid authorization. Checks if the response status code is 403,
        indicating forbidden access.

        Args:
            match_uri (str): The base URI for the matches resource.

        Returns:
            None
        """
        uri = f"{base_uri}/teams/759/matches"
        response = requests.get(uri)
        actual = response.json()

        expected = {
            "message": "The resource you are looking for is restricted and apparently not within your permissions. Please check your subscription.",
            "errorCode": 403
        }
        assert expected == actual

    def test_get_match_data_for_a_particular_team_with_an_invalid_token(self, base_uri, invalid_token):
        """
        Test the retrieval of match data for a single team with an invalid token.

        Sends a GET request to the '/v4/teams/759/matches' endpoint with an
        invalid header (token). Checks if the response status code is 400, indicating
        a bad request due to the invalid token.

        Args:
            match_uri (str): The base URI for the matches resource.
            invalid_token (dict): Invalid authentication token.

        Returns:
            None
        """
        uri = f"{base_uri}/teams/759/matches"
        response = requests.get(uri, headers=invalid_token)
        actual = response.json()

        expected = {
            "message": "Your API token is invalid.",
            "errorCode": 400
        }
        assert expected == actual

    def test_get_match_for_a_particular_competition(self, competition_uri, valid_token):
        """
        Test the retrieval of match data for a single competition.

        Sends a GET request to the '/v4/competitions/2003/matches?matchday=1' endpoint with
        the provided header, and it checks if the response status code is 200, indicating
        a successful request.

        Args:
            match_uri (str): The base URI for the matches resource.
            valid_token (dict): Valid authentication token.

        Returns:
            None
        """
        uri = f"{competition_uri}/2003/matches?matchday=1"
        response = requests.get(uri, headers=valid_token)
        assert response.status_code == 200
        actual = response.json()

        assert actual["filters"]["season"] == 2023
        assert actual["resultSet"]["played"] == 9
        assert actual["competition"]["id"] == 2003

