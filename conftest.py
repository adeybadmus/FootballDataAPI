import requests
from pytest import fixture

# Base URI for the Football API
uri = "https://api.football-data.org/v4"


@fixture(scope='function', autouse=True)
def base_uri():
    """
    Fixture to provide the URI for the persons resource.
    """
    return uri

@fixture(scope='function', autouse=True)
def person_uri():
    """
    Fixture to provide the URI for the persons resource.
    """
    return f"{uri}/persons"


@fixture(scope='function', autouse=True)
def area_uri():
    """
    Fixture to provide the URI for the areas resource.
    """
    return f"{uri}/areas"


@fixture(scope='function', autouse=True)
def competition_uri():
    """
    Fixture to provide the URI for the competitions resource.
    """
    return f"{uri}/competitions"


@fixture(scope='function', autouse=True)
def match_uri():
    """
    Fixture to provide the URI for the matches resource.
    """
    return f"{uri}/matches"


@fixture(scope='function', autouse=True)
def valid_token():
    """
    Fixture to provide a valid authentication token.
    """
    return {'X-Auth-Token': '8d07ed90c4484b2cb27482db2259328c'}


@fixture(scope='function', autouse=True)
def invalid_token():
    """
    Fixture to provide an invalid authentication token.
    """
    return {'X-Auth-Token': 'xxuqs77666'}


@fixture(scope='function', autouse=True)
def login_uri():
    """
    Fixture to provide the URI for the login resource.
    """
    return f"{uri}/client/login"


@fixture(scope='function', autouse=True)
def login_with_valid_token(login_uri, valid_token):
    """
    Fixture to simulate login with a valid token and return saved cookies.
    """
    response = requests.post(login_uri, valid_token)
    saved_cookies = response.cookies
    return saved_cookies


@fixture(scope='function', autouse=True)
def login_with_invalid_token(login_uri, invalid_token):
    """
    Fixture to simulate login with an invalid token and return saved cookies.
    """
    response = requests.post(login_uri, invalid_token)
    saved_cookies = response.cookies
    return saved_cookies
