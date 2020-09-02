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
            Add_New_Place()
            break
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
        line = Display_File.readline().strip().split(',')
        line[2] = int(line[2])
        print(f"  {Total}. {line[0]:10} in {line[1]:12} priority {line[2]:2}")
        # print(" {:}. {} in {} priority {}".format(Total, line[0], line[1], line[2]))
        Total += 1

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

def Add_New_Place():
    Display_File = open("places.csv", "a")
    Location_Input = str(input("Name: ").capitalize())
    while len(Location_Input) <= 0:
        print("Input cannot be blank")
        Location_Input = str(input("Name: ").capitalize())
    Country_Input = str(input("Country: ").capitalize())
    while len(Country_Input) <= 0:
        print("Input cannot be blank")
        Country_Input = str(input("Name: ").capitalize())
    Priority_Input = Integer_Error_Checking()
    print(f"{Location_Input} in {Country_Input} (priority {Priority_Input}) added to Travel Tracker")
    Display_File.write('\n')
    Display_File.write(f"{Location_Input},{Country_Input},{Priority_Input}")


def Integer_Error_Checking():
    Valid_Entry = False
    while not Valid_Entry:
        try:
            Priority_Input = int(input("Number?: "))
            Valid_Entry = True
        except ValueError:
            print("Not a number")
    return Priority_Input

main()
