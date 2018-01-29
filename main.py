#!/usr/bin/env python3
'''hostping'''
import subprocess
import platform


HOSTS = [
    ['pi', '192.168.192.27'],
    ['desktop', '192.168.2.2'],
]


def ping(sHost):
    try:
        subprocess.check_output("ping -{} 1 {}".format(
            'n' if platform.system().lower() == "windows" else 'c', sHost),
            shell=True)
    except Exception as e:
        return False

    return True

# figure out longest name and ip
# name_len = 6
# ip_len = 0
# for name, ip in HOSTS:
#     if len(name) > name_len:
#         name_len = len(name)
#     if len(ip) > ip_len:
#         ip_len = len(ip)
# print('-' * name_len)
# print(' ' * round((name_len - 4)/2) + 'name')

print("\n| Name           | IP              | Status")
print("-------------------------------------------")
for name, ip in HOSTS:
    print('| %-15s| %-16s| %6s' %
          (name, ip, 'Online' if ping(ip) else 'Offline'))
