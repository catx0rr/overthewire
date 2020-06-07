#!/usr/bin/env python

import base64
import json
import urllib.parse

# XOR Function from the PHP code on natas11

'''
function xor_encrypt($in, $key) {
    $text = $in;
    $outText = '';

    for ($i = 0; $i < strlen($text); $i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
'''

# XOR function converted to python

def xor_crypt(text, key=''):

    encrypted_text = ''

    # Iterate on the char per string on plaintext, and xor with key
    for i in range(len(text)):

        encrypted_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    return encrypted_text


# Default data, the known plaintext
default_data = {'showpassword': 'no', 'bgcolor': '#ffffff'}

# Convert dictionary to json string value
# plain_text = json.dumps(default_data)

plain_text = json.dumps(default_data, separators=(',', ':'))

# Cookie from the browser, also the ciphertext as per seen on the function saveData($d)
cookie_value = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D'

# Reverse the base64 encoding
cipher_text = base64.b64decode(urllib.parse.unquote(cookie_value)).decode('utf-8')

key = xor_crypt(plain_text, cipher_text)

print(key)
