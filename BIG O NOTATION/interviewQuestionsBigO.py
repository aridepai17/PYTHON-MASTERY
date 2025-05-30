################ Interview Questions #############

# Find the Time Complexity of the following code snippets 

#Question1
def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print("Sum = "+str(sum)+", Product = "+str(product))

ar1 = [1,2,3,4]
foo(ar1)

# Time Complexity: O(n)

#Question2
def printPairs(array):
    for i in array:
        for j in array:
            print(str(i)+","+str(j))
            
# Time Complexity: O(n^2)

#Question3
def printUnorderedPairs(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            print(array[i] + "," + array[j])
            
# Time Complexity: O(n^2)

#Question4
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))

arrayA = [1,2,3,4,5]
arrayB = [2,6,7,8]

# Time Complexity: O(n*m) where n is the length of arrayA and m is the length of arrayB

#Question5
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))

# printUnorderedPairss(arrayA,arrayB)
# Time Complexity: O(n*m) where n is the length of arrayA and m is the length of arrayB

#Question6
def reverse(array):
    for i in range(0,int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

reverse(arrayA)

# Time Complexity: O(n)

