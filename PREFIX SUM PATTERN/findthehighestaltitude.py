# LEETCODE 1732

'''
There is a biker going on a road trip.
The road trip consists of n+1 points at diffirent altitudes. 
The biker starts his trip on point 0 with altitude 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i +1 for
all 0 <= i < n (0-indexed)
Return the highest altitude of a point.
'''

def largestAltitude(gain):
    altitude = 0
    maxaltitude = 0
    
    for g in gain:
        altitude += g
        maxaltitude = max(maxaltitude, altitude)
    return maxaltitude

# Example usage:
gain = [-5, 1, 5, 0, -7]
print(largestAltitude(gain))  # Output: 1

# Another example:
gain = [1, 2, 3, 4, 5]
print(largestAltitude(gain))  # Output: 15

# Yet another example:
gain = [-2, -1, 0, 1, 2]
print(largestAltitude(gain))  # Output: 0