"""
Replace the contents of this module docstring with your own details
Name: Cooper Plath
Date started: 30-8-20
GitHub URL:
"""


def main():
    print("Travel Tracker 1.0 - by Cooper Plath")
    Menu_Input = Display_Menu()
    print(Menu_Input)


def Display_Menu():
    print(""" Menu:  
 L - List Places
 A - Add new place
 M - Mark a place as visited
 Q - Quit""")

    Menu_Input = str(input(" >>> "))
    while Menu_Input.isalpha() == False:
        print("Invalid")
        Menu_Input = str(input(" >>> "))
    return Menu_Input.upper()





main()
