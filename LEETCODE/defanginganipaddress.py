# LEETCODE 1108

'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
'''

def defanginganipaddress(address):
    return address.replace('.', '[.]')

# Example usage:
address = "1.1.1.1"
print(defanginganipaddress(address))  # Output: "1[.]1[.]1[.]1"

address = "237.84.2.178"
print(defanginganipaddress(address))  # Output: "255[.]100[.]50[.]0"

address = "237.84.2.178"
print(defanginganipaddress(address))  # Output: "255[.]100[.]50[.]0"