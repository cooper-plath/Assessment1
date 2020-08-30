"""
Replace the contents of this module docstring with your own details
Name: Cooper Plath
Date started: 30-8-20
GitHub URL:
"""


def main():

    print("Travel Tracker 1.0 - by Cooper Plath")
    Menu_Input = Display_Menu()
    """Run until the user presses Q"""
    while Menu_Input != "Q":
        # List places
        if Menu_Input == "L":
            print("List Places")
            Display_List_Options()
        # Add new place
        elif Menu_Input == "A":
            print("Add new place")
        # Mark a place as visited
        elif Menu_Input == "M":
            print("Mark a place as visited")
    else:
        print(f"{Read_Place_File()} places loaded from places.csv")
        print("Have a nice day :)")



def Display_List_Options():


def Read_Place_File():
    # Opens file and counts the amount entries added
    Display_File = open("places.csv", "r")
    Total_List_Items = 0
    for i in Display_File:
        Total_List_Items += 1
    Display_File.close()
    return Total_List_Items






def Display_Menu():

    print(f" {Read_Place_File()} places loaded from places.csv")
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
