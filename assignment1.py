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
            Menu_Input = Display_Menu()
            break
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
    Display_File = open("places.csv")
    Total = 1
    for line in range(Read_Place_File()):
        File_List = []
        line = Display_File.readline().strip().split(',')
        print(f"  {Total}. {line[0]} in {line[1]} priority {line[2]}")
        Total += 1

# def Print_File_List(File_List):
#     for i in File_List:
#         print()


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

    Menu_Input = str(input(" >>> ").upper())
    Program_Key_List = ['L', 'A', 'M', 'Q']
    while not Menu_Input in Program_Key_List:
        print("Invalid")
        Menu_Input = str(input(" >>> ").upper())
    return Menu_Input





main()
