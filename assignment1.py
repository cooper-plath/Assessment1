"""
Replace the contents of this module docstring with your own details
Name: Cooper Plath
Date started: 30-8-20
GitHub URL:
"""


def main():

    print("Travel Tracker 1.0 - by Cooper Plath")
    Menu_Input = Display_Menu()



def Read_Place_File():
    Display_File = open("places.csv", "r")
    Total_List_Items = 0
    for i in Display_File:
        Total_List_Items += 1
    Display_File.close()
    return Total_List_Items






def Display_Menu():
    File_Amount = Read_Place_File()
    print(f" {File_Amount} places loaded from places.csv")
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
