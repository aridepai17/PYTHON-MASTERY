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

# Additional examples
address1 = "192.168.1.1"
print(defanginganipaddress(address1))  # Output: "192[.]168[.]1[.]1"

address2 = "255.255.255.255"
print(defanginganipaddress(address2))  # Output: "255[.]255[.]255[.]255"

address3 = "0.0.0.0"
print(defanginganipaddress(address3))  # Output: "0[.]0[.]0[.]0"

address4 = "10.0.0.1"
print(defanginganipaddress(address4))  # Output: "10[.]0[.]0[.]1"

address5 = "172.16.254.1"
print(defanginganipaddress(address5))  # Output: "172[.]16[.]254[.]1"

address6 = "192.0.2.146"
print(defanginganipaddress(address6))  # Output: "192[.]0[.]2[.]146"

address7 = "203.0.113.195"
print(defanginganipaddress(address7))  # Output: "203[.]0[.]113[.]195"