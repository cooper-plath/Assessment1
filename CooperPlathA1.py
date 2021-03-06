"""
Replace the contents of this module docstring with your own details
Name: Cooper Plath
Date started: 30-8-20
GitHub URL: https://github.com/cooper-plath/Assessment1
"""

def main():
    Display_File = open("places.csv")
    Places_List = []
    # Reads places.csv file and adds information to list
    Add_File_Contents_To_List(Display_File, Places_List)
    print("Travel Tracker 1.0 - by Cooper Plath")
    Total_List_Items(Places_List)
    print(f" {Total_List_Items(Places_List)} places loaded from places.csv")
    Menu_Input = Display_Menu()
    """Run until the user presses Q"""
    while Menu_Input != "Q":
        # List places
        if Menu_Input == "L":
            Display_List_Options(Places_List)
            Menu_Input = Display_Menu()
        # Add new place
        elif Menu_Input == "A":
            Add_New_Place(Places_List)
            Menu_Input = Display_Menu()
        # Mark a place as visited
        elif Menu_Input == "M":
            Mark_Place_As_Visited(Places_List)
            Menu_Input = Display_Menu()
    else:
        Add_List_To_File(Places_List)
        print(f"{Total_List_Items(Places_List)} places saved to places.csv")
        print("Have a nice day :)")


def Add_List_To_File(Places_List):
    Save_To_File = open("Places.csv", "w")
    New_Row = 0
    for i in range(Total_List_Items(Places_List)):
        Save_To_File.write("{}, {}, {}, {} \n".format(Places_List[New_Row][0], Places_List[New_Row][1], Places_List[New_Row][2], Places_List[New_Row][3]))
        New_Row += 1
    Save_To_File.close()

def Add_File_Contents_To_List(Display_File, Places_List):
    for line in Display_File:
        line = line.strip()
        Line_Parts = line.split(',')
        Line_Parts[2] = int(Line_Parts[2])
        Places_List.append(Line_Parts)
    return Places_List


def Display_List_Options(Places_List):
    # Finds longest 'name' and 'location' strings as to dynamically format list
    Name_Length = Find_Name_String_Length(Places_List)
    Location_Length = Find_Location_String_Length(Places_List)
    Row_In_List = 1
    New_Line_In_List = 0
    Total_Places_Unvisited = 0
    for i in range(Total_List_Items(Places_List)):
        if Places_List[New_Line_In_List][3] == 'n':
            print(
                f" *{Row_In_List}. {Places_List[New_Line_In_List][0]:{Name_Length}} in {Places_List[New_Line_In_List][1]:{Location_Length}} priority {Places_List[New_Line_In_List][2]}")
            Total_Places_Unvisited += 1
        else:
            print(
                f"  {Row_In_List}. {Places_List[New_Line_In_List][0]:{Name_Length}} in {Places_List[New_Line_In_List][1]:{Location_Length}} priority {Places_List[New_Line_In_List][2]}")
        Row_In_List += 1
        New_Line_In_List += 1
    print(f" {Total_List_Items(Places_List)} places. You still want to visit {Total_Places_Unvisited} places. ")


def Find_Name_String_Length(Places_List):
    File_List_Entry = 0
    Max_Name_String = 0
    # Runs through each sublist in global list and to find longest string entry
    for i in range(Total_List_Items(Places_List)):
        if len(Places_List[File_List_Entry][0]) > Max_Name_String:
            Max_Name_String = len(Places_List[File_List_Entry][0])
        File_List_Entry += 1
    return Max_Name_String


def Find_Location_String_Length(Places_List):
    File_List_Entry = 0
    Max_Location_String = 0
    for i in range(Total_List_Items(Places_List)):
        if len(Places_List[File_List_Entry][1]) > Max_Location_String:
            Max_Location_String = len(Places_List[File_List_Entry][1])
        File_List_Entry += 1
    return Max_Location_String


def Total_List_Items(Places_List):
    # Counts how many entries are in list
    Total_List_Items = len(Places_List)
    return Total_List_Items


def Display_Menu():
    print(""" Menu:  
 L - List Places
 A - Add new place
 M - Mark a place as visited
 Q - Quit""")

    Menu_Input = str(input(" >>> ").upper())
    Program_Key_List = ['L', 'A', 'M', 'Q']
    # Error checking that user inputs correct key to navigate menu
    while not Menu_Input in Program_Key_List:
        print("Invalid menu choice")
        Menu_Input = str(input(" >>> ").upper())
    return Menu_Input


def Add_New_Place(Places_List):
    Location = Location_Error_Checking(Places_List)
    Country = Country_Error_Checking()
    Priority_Input = Integer_Error_Checking(Places_List)
    print(f"{Location} in {Country} (priority {Priority_Input}) added to Travel Tracker")
    # Inserts new sublist at beginning of global list once user enters correct information
    Places_List.insert(0, [Location, Country, Priority_Input, "n"])


def Mark_Place_As_Visited(Places_List):
    Display_List_Options(Places_List)
    # Checks if all locations have been visited already, prints message
    All_Visited = Check_If_Locations_Are_Visited(Places_List)
    if All_Visited == True:
        print(" No unvisited places")
    else:
        print(" Mark the number of a place to mark as visited")
        Mark_Visited = Mark_Visited_Input_Error_Check(Places_List)
        print(f" {Places_List[Mark_Visited][0]} in {Places_List[Mark_Visited][1]} visited!")
        # Once user marks location as visited, sublist element -1 is marked as visited
        Places_List[Mark_Visited][-1] = 'v'


def Check_If_Locations_Are_Visited(Places_List):
    # Runs through each sublist and checks if 'n', not visited is still in list
    New_Row = 0
    All_Visited = True
    for i in range(Total_List_Items(Places_List)):
        if 'n' in Places_List[New_Row][-1]:
            All_Visited = False
        else:
            New_Row += 1
    return All_Visited


def Mark_Visited_Input_Error_Check(Places_List):
    valid_integer = False
    while not valid_integer:
        try:
            Mark_Visited_Input = int(input(" >>> "))
            Mark_Visited_Input -= 1
            if Mark_Visited_Input < 0:
                print("Number must be > 0")
            elif (Mark_Visited_Input) > Total_List_Items(Places_List):
                print("Invalid place number")
            else:
                if Places_List[Mark_Visited_Input][-1] == 'v':
                    print("That place is already visited")
                else:
                    valid_integer = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return Mark_Visited_Input


def Integer_Error_Checking(Places_List):
    valid_integer = False
    while not valid_integer:
        try:
            Priority_Input = int(input("Priority: "))
            if Priority_Input <= 0:
                print("Number must be > 0")
            else:
                Input_In_List = Check_Priority_In_List(Priority_Input, Places_List)
                if Input_In_List == True:
                    print("Invalid place number")
                else:
                    valid_integer = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return Priority_Input


def Check_Priority_In_List(Priority_Input, Places_List):
    # Checks that priority input isn't identical to element in list
    Input_In_List = False
    Next_Row = 0
    for i in range(Total_List_Items(Places_List)):
        if int(Priority_Input) in Places_List[Next_Row]:
            Input_In_List = True
        else:
            Next_Row += 1
    return Input_In_List


def Check_Location_In_List(Location_Input, Places_List):
    # Checks that location input isn't identical to element in list
    Location_In_List = False
    Next_Row = 0
    for i in range(Total_List_Items(Places_List)):
        if Location_Input.capitalize() in Places_List[Next_Row]:
            Location_In_List = True
        else:
            Next_Row += 1
    return Location_In_List


def Location_Error_Checking(Places_List):
    # Error checking that str input isn't an integer or blank. Than checks if location is already in list
    Valid_Entry = False
    while not Valid_Entry:
        Location_Input = str(input("Name?: "))
        if len(Location_Input) <= 0:
            print("Can't be blank")
        elif Location_Input.isalpha() == False:
            print("Can't be a number")
        else:
            Location_In_List = Check_Location_In_List(Location_Input, Places_List)
            if Location_In_List == True:
                print("That place is already visited")
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
