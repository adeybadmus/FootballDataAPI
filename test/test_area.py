import requests
from unittest import TestCase
from config import HEADER, BASE_URL

class AreaTest(TestCase):
    """
    Test case for retrieving data related to areas.

    This test suite includes tests for:
    1. Getting data for all areas
    2. Getting data for a single area
    3. Getting data for a single area without a token
    4. Getting data for a single area with an invalid token
    """

    def test_get_data_for_all_areas(self):
        """
        Test the retrieval of data for all areas.

        This test sends a GET request to the '/v4/areas' endpoint and checks if
        the response status code is 200, indicating a successful request.
        """
        header = HEADER
        base_url = BASE_URL
        resource = "/v4/areas"
        url = base_url + resource
        response = requests.get(url, headers=header)
        print(response.text)
        assert response.status_code == 200

    def test_get_data_for_a_single_area(self):
        """
        Test the retrieval of data for a single area.

        This test sends a GET request to the '/v4/areas/2077' endpoint and checks
        if the response status code is 200, indicating a successful request.
        """
        header = HEADER
        base_url = BASE_URL
        resource = "/v4/areas/2077"
        url = base_url + resource
        response = requests.get(url, headers=header)
        print(response.text)
        assert response.status_code == 200

    def test_get_data_for_a_single_area_without_token(self):
        """
        Test the retrieval of data for a single area without a token.

        This test sends a GET request to the '/v4/areas/2077' endpoint without
        providing an authentication token. It checks if the response status code
        is 200, indicating a successful request.
        """
        base_url = BASE_URL
        resource = "/v4/areas/2077"
        url = base_url + resource
        response = requests.get(url)
        assert response.status_code == 200

    def test_get_data_for_a_single_area_with_invalid_token(self):
        """
        Test the retrieval of data for a single area with an invalid token.

        This test sends a GET request to the '/v4/areas/2077' endpoint with an
        invalid authentication token. It checks if the response status code is
        400, indicating a bad request due to the invalid token.
        """
        invalid_header = {'X-Auth-Token': 'X7886555DFT788'}
        base_url = BASE_URL
        resource = "/v4/areas/2077"
        url = base_url + resource
        response = requests.get(url, headers=invalid_header)
        print(response.text)
        assert response.status_code == 400
