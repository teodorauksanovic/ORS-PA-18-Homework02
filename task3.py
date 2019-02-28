"""
===================   TASK 3   ====================
* Name: Cube Volume
*
* Write a function `cube_volume` that will return
* volume of a cube for a given side length.
* If passed value is invalid, function should
* return -1 which indicates something went wrong.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""



def main():
    side_lenght = float(input('Enter a cube lenght:'))

    float(side_lenght)
    if float(side_lenght) < 0:
        print('-1')
        return main()
    else:
        print(side_lenght)

    cube_volume = float(side_lenght)**3
    print('Cube volume is', cube_volume)

main()
