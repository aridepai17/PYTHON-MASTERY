# LEETOCODE 1678

'''
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 
The interpreted strings are then concatenated in the original order.
Given the string command, return the Goal Parser's interpretation of command.
'''

def interpret(command):
    return command.replace('()', 'o').replace('(al)', 'al')

# Example usage:
command1 = "G()(al)"
print(interpret(command1))  # Output: "Goal"

command2 = "G()()()()(al)"
print(interpret(command2))  # Output: "Gooooal"

command3 = "(al)G(al)()()G"
print(interpret(command3))  # Output: "alGalooG"

command4 = "G(al)()G"
print(interpret(command4))  # Output: "GalG"