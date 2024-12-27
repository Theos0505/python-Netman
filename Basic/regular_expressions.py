import re
from random import choice

re_mac_address = r'^([0-9A-Fa-f]{2,4}[:-]?){5}([0-9A-Fa-f]{2,4})$'
# re_ip_address = (r'^(([0-9]|[1-9][0-9]|[1-9][0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}' + r'([0-9]|[1-9][0-9]|[1-9][0-9]{2}|2[0-4][0-9]|25[0-5])$')
re_ip_address = (r'^((2[0-4][0-9]|25[0-5]|[01]?[0-9][0-9]?)\.){3}' + r'(2[0-4][0-9]|25[0-5]|[01]?[0-9][0-9]?)')


# re_ip_address = (r'((\d{1,3})\.){3}' + r'(\d{1,3})$')  # This one is wrong for IP because it also accepts IP bits above 255

re_hostname = (r'(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])[_@])*' + r'([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])$')

def remark():
    return choice(['Nope!..Not the right one', 'whan...whan... Wrong!!!', 'Get it right Next time...'])


MAC_ADDRESS = 'mac-address'
IP_ADDRESS = 'ip address'
HOSTNAME = 'hostname'
EMAIL = 'email'
verify_list = [MAC_ADDRESS, IP_ADDRESS, HOSTNAME, EMAIL]
validation_pattern = {MAC_ADDRESS: re_mac_address,
                      IP_ADDRESS: re_ip_address,
                      HOSTNAME: re_hostname,
                      # EMAIL: re_email
                      }
for validation_type in verify_list:

    print(f'\n........{validation_type} verification.......')

    while True:
        input_to_validate = input("\nEnter the {} or <cr> to quit: ".format(validation_type))
        if not input_to_validate:
            break
        match = re.search(validation_pattern[validation_type], input_to_validate)
        if match is not None:
            print("\n---> Valid {}: {} at {}".format(validation_type, match
                                                     .group(0), match.start()))
        else:
            print("\n--->{}!!!! {}".format(input_to_validate, remark()))
