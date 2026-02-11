from reader import *

log_file = get_file_csv(FILE_NAME)

def ip_check(file):
    ip_external = []
    for log in file:
        if not (log[1].startswith('10.') or log[1].startswith('192.168')):
           ip_external.append(log)

    return ip_external

print(ip_check(log_file))
