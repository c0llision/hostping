#!/usr/bin/env python3
'''hostping'''
import subprocess
import platform


HOSTS = [
    ['pi', 'pi.c0llision'],
    ['desktop', 'desktop.c0llision'],
]


def ping(sHost):
    try:
        subprocess.check_output("ping -{} 1 {}".format(
            'n' if platform.system().lower() == "windows" else 'c', sHost),
            shell=True)
    except Exception as e:
        return False

    return True


def main():
    print("\n| Name           | IP              | Status")
    print("-------------------------------------------")
    for name, ip in HOSTS:
        print('| %-15s| %-16s| %6s' %
              (name, ip, 'Online' if ping(ip) else 'Offline'))


try:
    main()
except KeyboardInterrupt:
    pass
