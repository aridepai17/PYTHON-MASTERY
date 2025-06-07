# Write a function that calculates sum and product of all elements in a tuple of numbers.

def sumproduct(tuple1):
    sumtuple = 0
    producttuple = 1
    for i in tuple1:
        sumtuple += i
        producttuple *= i
    return sumtuple, producttuple

# Example usage:
tuple1 = (1, 2, 3, 4, 5)
print(sumproduct(tuple1))  # Output: (15, 120)


# Create a function that takes two tuples and returns a tuple containing element-wise sum of the two tuples.

def tupleelementsum(tuple2, tuple3):
    if len(tuple2) != len(tuple3):
        return "Tuples must have the same length"
    return tuple(map(sum, zip(tuple2, tuple3)))

# Example usage:
tuple2 = (5, 4, 3, 2, 1)
tuple3 = (1, 2, 3, 4, 5)
print(tupleelementsum(tuple2, tuple3))  # Output: (6, 6, 6, 6, 6)


# Write a function that takes a tuple and a value and returns a new tuple with the value inserted at the beginning of the tuple.

def insertvaluefront(tuple4, value):
    return (value,) + tuple4

# Example usage:
tuple4 = (2, 3, 4, 5)
print(insertvaluefront(tuple4, 1))  # Output: (1, 2, 3, 4, 5)


# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

def concatenate_strings(tuple5):
    return ' '.join(tuple5)

# Example usage:
tuple5 = ("Hello", "world", "from", "tuples")
print(concatenate_strings(tuple5))  # Output: "Hello world from tuples"


# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input tuple.

def get_diagonal(tup):
    return (tuple(tup[i][i] for i in range(len(tup))))

# Example usage:
tup = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(get_diagonal(tup))  # Output: (1, 5, 9)   


# Write a function that takes two tuples and returns a tuple containing the common elements of both tuples.

def commonelements(tuple6, tuple7):
    return tuple(set(tuple6) & set(tuple7))

# Example usage:
tuple6 = (1, 2, 3, 4, 5)
tuple7 = (4, 5, 6, 7, 8)
print(commonelements(tuple6, tuple7))  # Output: (4, 5)