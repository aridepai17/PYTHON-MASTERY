# LEETCODE 1556

# Given an integer n, add a dot (".") as the thousands separator to it and return it as a string.

def thousandSeparator(n):
  return f"{n:,}".replace(",", ".")

# Example usage
n1 = 987
print(thousandSeparator(n1))  # Output: "987"

# Additional examples
n2 = 1234
print(thousandSeparator(n2))  # Output: "1.234"

n3 = 123456
print(thousandSeparator(n3))  # Output: "123.456"

n4 = 1234567
print(thousandSeparator(n4))  # Output: "1.234.567"

n5 = 0
print(thousandSeparator(n5))  # Output: "0"

n6 = 1000
print(thousandSeparator(n6))  # Output: "1.000"

n7 = 1000000
print(thousandSeparator(n7))  # Output: "1.000.000"

n8 = 987654321
print(thousandSeparator(n8))  # Output: "987.654.321"

n9 = 10
print(thousandSeparator(n9))  # Output: "10"

n10 = 1000000000
print(thousandSeparator(n10))  # Output: "1.000.000.000"