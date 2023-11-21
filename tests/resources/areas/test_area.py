import requests
from pytest import mark

@mark.area
class AreaTests():
    """
    Test case for retrieving data related to areas.

    This tests suite includes tests for:
    1. Getting data for all areas
    2. Getting data for a single area
    3. Getting data for a single area without a token
    4. Getting data for a single area with an invalid token
    """

    def test_get_data_for_all_areas(self, area_uri, valid_token):
        """
        Test the retrieval of data for all areas.

        This tests sends a GET request to the '/v4/areas' endpoint and checks if
        the response status code is 200, indicating a successful request.
        """
        response = requests.get(area_uri, headers=valid_token)
        print(response.text)
        assert response.status_code == 200

    def test_get_data_for_a_single_area(self, area_uri, valid_token):
        """
        Test the retrieval of data for a single area.

        This tests sends a GET request to the '/v4/areas/2077' endpoint and checks
        if the response status code is 200, indicating a successful request.
        """
        area_id = "/2077"
        uri = area_uri + area_id
        response = requests.get(uri, headers=valid_token)
        print(response.text)
        assert response.status_code == 200

    def test_get_data_for_a_single_area_without_token(self, area_uri):
        """
        Test the retrieval of data for a single area without a token.

        This tests sends a GET request to the '/v4/areas/2077' endpoint without
        providing an authentication token. It checks if the response status code
        is 200, indicating a successful request.
        """
        area_id = "/2077"
        uri = area_uri + area_id
        response = requests.get(uri)
        assert response.status_code == 200

    def test_get_data_for_a_single_area_with_invalid_token(self, area_uri, invalid_token):
        """
        Test the retrieval of data for a single area with an invalid token.

        This tests sends a GET request to the '/v4/areas/2077' endpoint with an
        invalid authentication token. It checks if the response status code is
        400, indicating a bad request due to the invalid token.
        """
        area_id = "/2077"
        uri = area_uri + area_id
        response = requests.get(uri, headers=invalid_token)
        print(response.text)
        assert response.status_code == 400
