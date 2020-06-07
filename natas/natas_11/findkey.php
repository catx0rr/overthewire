#!/usr/bin/php

<?php

# Function from natas11 xor cipher

function xor_crypt($in, $key) {

    $text = $in;
    $outText = '';

    for ($i = 0; $i < strlen($text); $i++) {

        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

// Known plaintext
$defaultData = ["showpassword" => "no", "bgcolor" => "#ffffff"];

// Array to json string
$plainText = json_encode($defaultData);

// echo $plainText;

// Cookie value from the browser, also the Ciphertext
$cookieValue = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D';

// Reverse the base64 encoding
$cipherText = base64_decode(urldecode($cookieValue));

$key = xor_crypt($plainText, $cipherText);

echo $key;


