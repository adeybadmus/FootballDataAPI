import requests
from config import BASE_URL, HEADER


def login():
    login_url = BASE_URL + '/client/login'
    header = HEADER

    res = requests.post(login_url, header)

    saved_cookies = res.cookies
    print(saved_cookies)

def invalid_login():
    login_url = BASE_URL + '/client/login'
    invalid_header = {'X-Auth-Token': '55673hhjjjjkjkdd'}

    res = requests.post(login_url, invalid_header)

    saved_cookies = res.cookies
    print(saved_cookies)

