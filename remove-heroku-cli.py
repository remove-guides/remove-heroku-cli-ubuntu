#!/bin/python3

import subprocess
import os
import sys

USER = os.environ.get("SUDO_USER")
HOME = f'/home/{USER}'
RED = "\033[31m"


def remove_keys():
    try:
        list_keys_result = subprocess.check_output(
            ['apt-key list'], shell=True).decode(sys.stdout.encoding).split('\n')

        for index, line in enumerate(list_keys_result):

            if('heroku' in line):
                previous_line = (list_keys_result[index - 1]).split(' ')
                key = previous_line[-2] + previous_line[-1]

                os.system(f'apt-key del {key}')
    except:
        print(f"\n{RED} Failed on remove Heroku keys! \n")


def remove_files():
    try:
        os.system('rm -rf /usr/bin/heroku')
        os.system(f'rm -rf {HOME}/.cache/heroku')
        os.system(f'rm -rf {HOME}/.local/share/heroku')
        os.system('rm -rf /usr/lib/heroku')
        os.system('rm -rf /usr/local/bin/heroku')
        os.system('rm -rf /usr/local/lib/heroku')
        os.system('rm -rf /usr/local/heroku')
        os.system('rm -rf $XDG_DATA_HOME')
        os.system('rm -rf $XDG_CACHE_HOME')
    except:
        print(f"\n{RED} Failed on remove files! \n")


def remove_from_apt():
    try:
        os.system('apt-get purge heroku -y')
        os.system('rm -rf /etc/apt/sources.list.d/heroku.list')
    except:
        print(f"\n{RED} Failed on remove from apt! \n")


def main():
    remove_files()
    remove_from_apt()
    remove_keys()


if __name__ == '__main__':
    user_type = os.getuid()

    if(user_type != 0):
        print(f"\n{RED} Please Run as Root! \n")
        sys.exit(1)

    main()
