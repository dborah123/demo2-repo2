"""
loops.py

Description:
    Examples of different for loops sorted by data type
    1. Integers/static values
    2. Strings
    3. Lists
"""

""" INTEGERS """
def integer_loop():
    # Iterates thru loop 10 times adding by i to result and prints result
    integer = 10
    result = 0
    
    for i in range(integer):
        result += i
    print(result) # output: 45

""" STRINGS """
def string_loop_1():
    # Iterates thru string, adding character to end of new_string and printing after
    input_string = "hello"
    new_string = ""

    for char in input_string:
        new_string += char
    
    print(new_string) # output: hello

def string_loop_2():
    # Does same as `string_loop_1`
    input_string = "hello"
    new_string = ""

    for i in range(len(input_string)):
        new_string += input_string[i]
    
    print(new_string) # output: hello


""" LISTS """
def list_loop_1():
    # Takes list, multiplies each item by 2 and prints final result
    input_list = [1,2,3,4]

    for i in range(len(input_list)):
        input_list[i] *= 2
    
    print(input_list) # output: [2,4,6,8]

def list_loop_2():
    # Same as `list_loop_1` yet item does not actually get multiplied by 2
    input_list = [1,2,3,4]

    for item in input_list:
        item *= 2
        # Items are still able to be accessed this way and is still useful!!

    print(input_list) # output: [1,2,3,4]
    

def print_formatter(title):# Helper function
    print(f"\n**********************************************\n{title}\n")


def main():

    print_formatter("integer_loop:")

    integer_loop()

    print_formatter("string_loop_1:")

    string_loop_1()

    print_formatter("string_loop_2:")

    string_loop_2()

    print_formatter("list_loop_1:")

    list_loop_1()

    print_formatter("list_loop_2:")

    list_loop_2()

main()