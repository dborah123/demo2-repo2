"""
functions.py
NAME: Dan
DATE: 1/30/22

Questions:
- 
"""


"""
Note: I can put commas here if I want. This looks bad but if you have a really long function header
      it looks nicer
"""
def format_name_age(
    name,
    age
):
    """
    Parameters:
    name: string representing name
    age: integer representing age

    returns string formatted as desired
    """

    # Checks if user didn't supply string (note the syntax... no =="")
    if (not name):
        print("You didn't supply a name")
    else: # Return a formatted string using an 'f' string (not necessary but helpful)
        return f"My name is {name} and my age is {age}"

def is_old_enough(age):
    """
    Parameters:
    age: integer representing age

    returns: bool True if older than 18
    """

    # Checks if person is older enough
    if (age >= 18):
        return True

    return False


if __name__ == "main":
    """
    This is the main method. Python will begin executing the lines below first
    """
    # Define person1
    person1_name = "Joe"
    person1_age = 12

    # Print Joe's name
    bool = is_old_enough(person1_age)
    if (bool):
        formatted_string = format_name_age(person1_name, person1_age)
        print(formatted_string)


    # Define person2
    person2_name = "Jane"
    person2_age = 20

    # Print Jane's name
    """
    Note: I didn't use extra variables this time, just the functions returning. 
          Either way is OK
    """
    if (is_old_enough(person2_age)):
        print(format_name_age(person2_name, person2_age))


    """
    Output:
    My name is Jane and my age is 20
    """