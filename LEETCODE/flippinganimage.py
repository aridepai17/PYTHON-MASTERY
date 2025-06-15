# LEETCODE 832

'''
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0,1,1] results in [1,0,0].
'''

def flipAndInvertImage(image):
    result = []
    
    for row in image:
        flippedAndInverted = [ 1 - bit for bit in reversed(row) ]
        result.append(flippedAndInverted)
    return result

# Example usage
image1 = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(flipAndInvertImage(image1))  # Output: [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

# Additional examples
image2 = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
print(flipAndInvertImage(image2))  # Output: [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

image3 = [[0, 0], [0, 0]]
print(flipAndInvertImage(image3))  # Output: [[1, 1], [1, 1]]

image4 = [[1, 1], [1, 1]]
print(flipAndInvertImage(image4))  # Output: [[0, 0], [0, 0]]

image5 = [[1]]
print(flipAndInvertImage(image5))  # Output: [[0]]

image6 = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
print(flipAndInvertImage(image6))  # Output: [[1, 0, 1], [0, 1, 0], [1, 0, 1]]