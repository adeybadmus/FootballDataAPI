import requests
from config import BASE_URL, USERNAME, PASSWORD

login_url = BASE_URL + '/client/login'
login_data = {'username': USERNAME, 'password': PASSWORD}

res = requests.post(login_url, json=login_data)

saved_cookies = res.cookies
print(saved_cookies)

if res.json().get('success'):
    print('Login successful!')
else:
    print('Login failed!')


protected_url = BASE_URL + 'client/home'

res= requests.get(protected_url, cookies=saved_cookies)

if res.json().get('success'):
    print('Access granted!')
else:
    print('Access denied!')
