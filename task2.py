"""
===================   TASK 2   ====================
* Name: Convert Kilometers To Miles
*
* Write a script that will convert kilometers to
* miles. Script should ask user for input and check
* if user input is valid. If not, the script should
* quit immediately with appropriate message.
*
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Note: You may use `can_string_be_float` function
* from previous task to validate user input.
===================================================
"""


def can_string_be_float(user_value):
    allowed_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

    for ch in user_value:
        if ch not in allowed_characters:
            return False

        number_of_dots = 0

        for ch in user_value:
            if ch == '.':
                number_of_dots = number_of_dots + 1

        if number_of_dots > 1:
            return False

    return True



def main():
    user_value = float(input("Enter a distance in miles: "))

    conversionfactor = 1.609
    kilometers = user_value * conversionfactor

    if can_string_be_float(user_value):
        print("The distance in kilometers is: ", kilometers)
    else:
        print("User value is not valid.")
main()