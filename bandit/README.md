# Solution

---

- bandit0
    - ``` cat readme ```

- bandit1
    - ``` file ./- ```
    - ``` file $(pwd)/- ```
    - ``` cat $(pwd)/- ```

- bandit2
    - ``` cat spaces\ in\ this\ filename```
    - ``` cat "spaces in this filename"```

- bandit3
    - ``` find inhere/ -type f -name '.*'```
    - ``` find inhere/ -type f -name '.*' -exec cat {} \;```
    - ``` find inhere/ -type f -name \.\* -exec cat {} \;```

- bandit4
    - ``` find . -type f -exec file {} \;```
    - ``` find . -type f -name -file07 -exec cat {} \;```
    - ``` find . -type f -name -file* -exec strings {} \;```

- bandit5
    - ```find inhere/ -type f ! -executable -size 1033c | xargs head -n1```
    - ```find inhere/ -type f ! -executable -size 1033c -exec head -n1 {} +```

- bandit6
    - ```find / -type f -user bandit7 -group bandit6 -size 33c -exec cat {} \; 2>/dev/null```
    - ```find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null | xargs cat```

- bandit7
    - ```cat data.txt | grep millionth | awk '{print $2}'```
    - ```awk '/^millionth/ {print $2}' data.txt```

- bandit8
    - ```cat data.txt | sort | uniq -u```
    - ```cat data.txt | sort | uniq -c | tail -n14 | head -n1 | awk '{print $2}'```

- bandit9
    - ```strings data.txt | grep '^.*==.*[a-zA-Z]$' | tail -n1 | cut -d' ' -f2```
    - ```strings data.txt | grep '==.*' | tail -n1 | awk '{print $2}'```

- bandit10
    - ```cat data.txt | base64 -d | awk '{print $4}'```
    - ```base64 -d data.txt | cut -d' ' -f4```

- bandit11
    - ```cat data.txt | tr A-Za-z N-ZA-Mn-za-m | awk '{print $4}'```
    - ```tr A-Za-z N-ZA-Mn-za-m < data.txt | cut -d' ' -f4```

- bandit12
    - ```mkdir /tmp/catx```
    - ```cat data.txt | xxd -r > /tmp/catx/file```
    - ```gunzip -c file > file2```
    - ```bzip2 -dc file2 > file3```
    - ```bzip2 -dc file3 > file4```
    - ```bzip2 -dc file4 > file5```
    - ```gunzip -c file5 > file6```
    - ```tar -xvf file6```
    - ```tar -xvf data5.bin```
    - ```tar -xvf data6.bin```
    - ```bzip2 -dc data6.bin > file7```
    - ```tar -xvf file7```
    - ```gunzip -c data8.bin > data9.bin```
    - ```cat data9.bin | awk '{print $4}'```

- bandit13 
    - ```ssh bandit14@localhost -i sshkey.private```
    - ```find /etc/bandit_pass/ -type f -user bandit14 -perm -400 | xargs cat```

- bandit14
    - ```echo "4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e" | nc localhost 30000 | tr '\n' ' ' | cut -d' ' -f2```

- bandit15
    - ```echo 'BfMYroe26WYalil77FoDi9qh59eK5xNr' | openssl s_client -connect 127.0.0.1:30001 -quiet -ign_eof | tr '\n' ' ' | cut -d' ' -f2```

- bandit16
    - ```nc -z -v 127.0.0.1 31000-32000```
    - ```nmap -sV -p 31000-32000 127.0.0.1```
    - ```echo 'cluFn7wTiGryunymYOu4RcffSxQluehd' | openssl s_client -connect 127.0.0.1:31790 -quiet -ign_eof > /tmp/id_rsa```
    - ```chmod 600 /tmp/id_rsa```
    - ```ssh -i /tmp/id_rsa bandit17@127.0.0.1```
    - ```find /etc/bandit_pass/ -user bandit17 -perm -400 | xargs cat```

- bandit17
    - ```diff passwords.old passwords.new | tail -n1 | cut -d ' ' -f2```

- bandit18
    - ```ssh -p 2220 -t bandit18@bandit.labs.overthewire.org /bin/sh```
    - ```ssh -p 2220 bandit18@bandit.labs.overthewire.org "bash --norc"```
    - ```cat readme```

- bandit19
    - ```./bandit20-do cat /etc/bandit_pass/bandit20```

- bandit20
    - ```find /etc/bandit_pass/ -type f -perm -400 -user bandit20 | xargs cat | nc -lvp 1337```
    - ```./suconnect 1337```

- bandit21
    - ``` find /etc/cron.d/ -type f -exec grep bandit22 {} +```
    - ```cat /usr/bin/cronjob_bandit22.sh```
    - ```cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv```

- bandit22
    - ```find /etc/cron.d/ -type f -user root -exec grep bandit23 {} + && find /usr/bin -user bandit23 -exec cat {} \;```
    - ```echo I am user bandit23 | md5sum | awk '{print $1}' | xargs echo /tmp/ | sed 's/ //g' | xargs cat```

- bandit23
    -