from reader import *

log_file = get_file_csv(FILE_NAME)

# def ip_check_external(file):
#     ip_external = []
#     for log in file:
#         if not (log[1].startswith('10.') or log[1].startswith('192.168')):
#            ip_external.append(log)
#
#     return ip_external
#
# print(ip_check_external(log_file))


def ip_check_sensitive_port(file):
    ip_port = []
    sensitive_port = ['22', '23', '3389']
    for log in file:
        if log[3] in sensitive_port:
            ip_port.append(log)

    return ip_port

print(ip_check_sensitive_port(log_file))