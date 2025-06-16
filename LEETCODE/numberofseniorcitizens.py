# LEETCODE 2678

'''
You are given a 0-indexed array of strings details.
Each element of details provides information about a given passenger compressed into a string of length 15. 

The system is such that:
1. The first ten characters consist of the phone number of passengers.
2. The next character denotes the gender of the person.
3. The following two characters are used to indicate the age of the person.
4. The last two characters determine the seat allotted to that person.

Return the number of passengers who are strictly more than 60 years old.
'''

def countSenior(details):
    count = 0
    for info in details:
        if int(info[11:13]) > 60:
            count += 1
    return count

# Example usage
details1 = ["7868190123M1200", "1234567890F6500", "9876543210M7000"]
print(countSenior(details1))  # Output: 1

# Additional examples
details2 = ["1234567890M2500", "0987654321F4500", "1122334455M6100"]
print(countSenior(details2))  # Output: 2

details3 = ["1234567890M6100", "0987654321F6200", "1122334455M5900"]
print(countSenior(details3))  # Output: 2 (Both 61 and 62 are seniors)

details4 = ["1234567890M6000", "0987654321F6000", "1122334455M6000"]
print(countSenior(details4))  # Output: 0 (All are exactly 60)

details5 = ["1234567890M7000", "0987654321F8000", "1122334455M9000"]
print(countSenior(details5))  # Output: 3 (All are seniors)

details6 = ["1234567890M3000", "0987654321F2500", "1122334455M4000"]
print(countSenior(details6))  # Output: 0 (All are under 60)

details7 = ["1234567890M6100", "0987654321F6100", "1122334455M6200", "2233445566M6300"]
print(countSenior(details7))  # Output: 4 (All are seniors)

details8 = ["1234567890M5900", "0987654321F5800", "1122334455M5700"]
print(countSenior(details8))  # Output: 0 (All are under 60)