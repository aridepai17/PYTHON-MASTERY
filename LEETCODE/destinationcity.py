# LEETCODE 1436

'''
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. 
Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
'''

def destCity(paths):
    starts = set()
    
    for start, end in paths:
        starts.add(start)
    
    for start, end in paths:
        if end not in starts:
            return end

# Example usage
paths1 = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
print(destCity(paths1))  # Output: "Sao Paulo"

# Additional examples
paths2 = [["A", "B"]]
print(destCity(paths2))  # Output: "B"

paths3 = [["A", "B"], ["B", "C"]]
print(destCity(paths3))  # Output: "C"

paths4 = [["X", "Y"], ["Y", "Z"], ["Z", "W"]]
print(destCity(paths4))  # Output: "W"

paths5 = [["Beijing", "Shanghai"], ["Shanghai", "Guangzhou"], ["Guangzhou", "Shenzhen"]]
print(destCity(paths5))  # Output: "Shenzhen"

paths6 = [["a", "b"], ["b", "c"], ["c", "d"], ["d", "e"]]
print(destCity(paths6))  # Output: "e"

paths7 = [["start", "mid1"], ["mid1", "mid2"], ["mid2", "end"]]
print(destCity(paths7))  # Output: "end"

paths8 = [["alpha", "beta"], ["beta", "gamma"], ["gamma", "delta"], ["delta", "epsilon"]]
print(destCity(paths8))  # Output: "epsilon"

paths9 = [["one", "two"], ["two", "three"], ["three", "four"], ["four", "five"], ["five", "six"]]
print(destCity(paths9))  # Output: "six"

paths10 = [["red", "blue"], ["blue", "green"], ["green", "yellow"]]
print(destCity(paths10))  # Output: "yellow"