# LEETCODE 2469

'''
You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.
You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].
Return the array ans. Answers within 10^-5 of the actual answer will be accepted.

Note that:
Kelvin = Celsius + 273.15
Fahrenheit = Celsius * 1.80 + 32.00
'''

def convertTemperature(celsius):
    return [celsius + 273.15, celsius * 1.80 + 32.00]

# Example usage
celsius1 = 36.50
print(convertTemperature(celsius1))  # Output: [309.65, 97.7]

# Additional examples:
celsius2 = 0.00
print(convertTemperature(celsius2))  # Output: [273.15, 32.0]

celsius3 = 100.00
print(convertTemperature(celsius3))  # Output: [373.15, 212.0]

celsius4 = -40.00
print(convertTemperature(celsius4))  # Output: [233.15, -40.0]

celsius5 = 25.00
print(convertTemperature(celsius5))  # Output: [298.15, 77.0]

celsius6 = 37.00
print(convertTemperature(celsius6))  # Output: [310.15, 98.6]

celsius7 = 15.50
print(convertTemperature(celsius7))  # Output: [288.65, 59.9]

celsius8 = 50.00
print(convertTemperature(celsius8))  # Output: [323.15, 122.0]