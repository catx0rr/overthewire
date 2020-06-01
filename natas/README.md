# Solution

---

- natas0
    - ```Login to web:```
    - ```inspec element the page and look for comments```

- other solution:
    - ```view-source:http://natas0.natas.labs.overthewire.org/```

- automated:
    - ```wget --user=natas0 --password=natas0 -q -O - http://natas0.natas.labs.overthewire.org/ | grep -oe '<!--[A-Za-z].*' | cut -d ' ' -f6```

- natas1
    - ```Login to web:```
    - ```view-source:http://natas0.natas.labs.overthewire.org/```

- automated:
    - ```curl -sv http://natas1.natas.labs.overthewire.org --user natas1:gtVrDuiDfck831PqWsLEZy5gyDz1clto | grep -o '<!--[A-Za-z].*' | awk '{print $6}'```
- python:
    - ```[solve.py]```

- natas2
    - ```Login to web:```
    - ```view-source:http://natas2.natas.labs.overthewire.org```
    - ```click on files/pixel.png```
    - ```go back one directory and found users.txt```

- automated:
    - ```curl -sv http://natas2.natas.labs.overthewire.org/files/users.txt --user natas2:ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi | grep natas3 | awk -F: '{print $2}'```

- natas3
    - ```Login to web:```
    - ```view-source:http://natas3.natas.labs.overthewire.org```
    - ```HINT:Not even Google will find it this time...```
    - ```http://natas3.natas.labs.overthewire.org/robots.txt```
    - ```Found: /s3cr3t/```
    - ```http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt```

- automated:
    - ```curl -sv http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt --user natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14 | grep natas4 | cut -d':' -f2```

- natas4
    -
