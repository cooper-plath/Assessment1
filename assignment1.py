"""
Replace the contents of this module docstring with your own details
Name: Cooper Plath
Date started: 30-8-20
GitHub URL:
"""


def main():
    Places_List = []
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
            Menu_Input = Display_Menu()
        # Mark a place as visited
        elif Menu_Input == "M":
            print("Mark a place as visited")
    else:
        print(f"{Read_Place_File()} places loaded from places.csv")
        print("Have a nice day :)")




def Display_List_Options():
    Display_File = open("places.csv")
    File_List = []
    for line in range(3):
        line = Display_File.readline().strip()
        File_List.append(line)
    List_Item = 0
    Row_In_List = 1
    for i in range(Read_Place_File()):
        Line_Parts = File_List[List_Item].split(',')
        Line_Parts[2] = int(Line_Parts[2])
        if Line_Parts[3] == 'n':
            print(f"*{Row_In_List}. {Line_Parts[0]} in {Line_Parts[1]} priority {Line_Parts[2]}")
        else:
            print(f" {Row_In_List}. {Line_Parts[0]} in {Line_Parts[1]} priority {Line_Parts[2]}")
        Row_In_List += 1
        List_Item += 1



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
    Location = Location_Error_Checking()
    Country = Country_Error_Checking()
    Priority_Input = Integer_Error_Checking()
    print(f"{Location} in {Country} (priority {Priority_Input}) added to Travel Tracker")
    # Display_File.write('\n')
    # Display_File.write(f"{Location},{Country},{Priority_Input}, {str('n')}")


def Integer_Error_Checking():
    valid_integer = False
    while not valid_integer:
        try:
            Priority_Input = int(input("Number?: "))
            valid_integer = True
        except ValueError:
            print("Not a number")
    return Priority_Input

def Location_Error_Checking():
    Valid_Entry = False
    while not Valid_Entry:
        Location_Input = str(input("Name?: "))
        if len(Location_Input) <= 0:
            print("Can't be blank")
        elif Location_Input.isalpha() == False:
            print("Can't be a number")
        else:
            Valid_Entry = True

    return Location_Input.capitalize()

def Country_Error_Checking():
    Valid_Entry = False
    while not Valid_Entry:
        Country_Input = str(input("Country?: "))
        if len(Country_Input) <= 0:
            print("Can't be blank")
        elif Country_Input.isalpha() == False:
            print("Can't be a number")
        else:
            Valid_Entry = True

    return Country_Input.capitalize()

main()
