
import csv

# Display_File = open('places.csv')
# for line in Display_File:
#     File_Line = line.rstrip().split('\t')
#     File_List.append(File_Line)
#     # Total = 0
#     # print(f"{Total}. {File_List[0]} in {File_List[1]} priority {File_List[2]}")
#     # Total += 1
#     print(File_List[0])


# Display_File = open('places.csv')
# File_List = []
# for line in Display_File:
#     File_Line = line.rstrip().split(',')
#     File_List.append(File_Line)
# print(File_List)


# Line = Display_File.readline().strip().split(',')


# Display_File = open('places.csv')
# # Line = Display_File.readline().strip().split(',')
# # print(Line)
# Total = 1
# for line in range(3):
#     File_List = []
#     line = Display_File.readline().strip().split(',')
#     print(f"{Total}. {line[0]} in {line[1]} priority {line[2]}")
#     Total += 1

# Interger error checking

# Valid_Entry = False
# while not Valid_Entry:
#     try:
#         Priority_Input = int(input("Number?: "))
#         Valid_Entry = True
#     except ValueError:
#         print("Not a number")
# print("Sick")

# String error checking

# Valid_Entry = False
# while not Valid_Entry:
#     try:
#         Priority_Input = str(input("Word?: "))
#         if Priority_Input.isalpha():
#             Valid_Entry = True
#     except:
#
#         print("Not a word")
# print("Sick")
# Valid_Entry = False
# while not Valid_Entry:
#     String_Input = str(input("Word?: "))
#     if len(String_Input) <= 0:
#         print("Can't be blank")
#     elif String_Input.isalpha() == False:
#         print("Can't be a number")
#     else:
#         Valid_Entry = True

# while not String_Input.isalpha():


# Display_File = open("places.csv")
# Total = 1
# for line in range(3):
#
#         line = Display_File.readline().strip().split(',')
#         line[2] = int(line[2])
#         if line[3] == 'n':
#             print(f"  *{Total}. {line[0]:10} in {line[1]:12} priority {line[2]:2}")
#         else:
#             print(f"   {Total}. {line[0]:10} in {line[1]:12} priority {line[2]:2}")
#         # print(" {:}. {} in {} priority {}".format(Total, line[0], line[1], line[2]))
#         Total += 1

# Display_File = open("places.csv")
# File_Line_List = []
# for line in Display_File:
#
#     Line_Parts = line.strip().split(',')
#     File_Line_List.append(Line_Parts)
# print(File_Line_List[0])
# Individual_List = File_Line_List[0]


# Display_File = open("places.csv")
# File_List = []
# for line in Display_File:
#     line = Display_File.readline()
#     line = line.strip().split(',')
#     File_List.append(line)
# print(File_List)



# Display_File = open("places.csv")
# File_List = []
# for i in range(3):
#     File_List.append(Display_File.readline().strip())
# print(File_List)
# Split_List_Item = File_List[0].split(',')
# print(Split_List_Item[2])
# Total = 0
# for i in range(3):
#     print(File_List[Total])
#     Total += 1




    # if Line_Parts[3] == 'n':
    #     print(f"*{Row_In_List}. {Line_Parts[0]:8} in {Line_Parts[1]:11} priority {Line_Parts[2]}")
    # else:
    #     print(f" {Row_In_List}. {Line_Parts[0]:} in {Line_Parts[1]:11} priority {Line_Parts[2]}")
    # print("{}. {} in {} priority {}".format(Row_In_List, Line_Parts[0], Line_Parts[1], Line_Parts[2]))
    # print(f"Line Part 0 {Line_Parts[0]}")
    # print(f"{Row_In_List}. {Line_Parts[0]:} in {Line_Parts[1]} priority {Line_Parts[2]}")




# def main():
#     Display_File = open("places.csv")
#     File_List = []
#
#
#     for line in range(3):
#         line = Display_File.readline().strip()
#         File_List.append(line)
#
#     File_List_Entry = 0
#     Row_In_List = 1
#     for i in range(3):
#         Line_Parts = File_List[File_List_Entry].split(',')
#         Line_Parts[2] = int(Line_Parts[2])
#         Name_Length = Max_Name_String_Length(Line_Parts)
#         Location_Length = Max_Location_String_Length(Line_Parts)
#         # if len(Line_Parts[0]) > Max_Name_String:
#         #     Max_Name_String = len(Line_Parts[0])
#         # if len(Line_Parts[1]) > Max_Location_String:
#         #     Max_Location_String = len(Line_Parts[1])
#         print(f"{Row_In_List}. {Line_Parts[0]:{Name_Length}} in {Line_Parts[1]:{Location_Length}} priority {Line_Parts[2]}")
#         Row_In_List += 1
#         File_List_Entry += 1

    # print(Name_Length)
    # print(Max_Location_String)


# def Max_Name_String_Length(Line_Parts):
#     Max_Name_String = 0
#     for i in range(3):
#
#         if len(Line_Parts[0]) > Max_Name_String:
#             Max_Name_String = len(Line_Parts[0])
#
# def Max_Location_String_Length(Line_Parts):
#     Max_Location_String = 0
#     for i in range(3):
#         if len(Line_Parts[1]) > Max_Location_String:
#             Max_Location_String = len(Line_Parts[1])

# main()

#
# def Main():
#     Display_File = open("places.csv")
#     File_List = []
#     for line in range(3):
#         line = Display_File.readline().strip()
#         File_List.append(line)
#     Name_Length = Find_Name_String_Length(File_List)
#     Location_Length = Find_Location_String_Length(File_List)
#     Row_In_List = 1
#     Split_Line = 0
#     for a in range(3):
#         Line_Parts = File_List[Split_Line].split(',')
#         Line_Parts[2] = int(Line_Parts[2])
#         print(
#             f"{Row_In_List}. {Line_Parts[0]:{Name_Length}} in {Line_Parts[1]:{Location_Length}} priority {Line_Parts[2]}")
#         Split_Line += 1
#         Row_In_List += 1
#
#
#
# def Find_Name_String_Length(File_List):
#     File_List_Entry = 0
#
#     Max_Name_String = 0
#     for i in range(3):
#         Line_Parts = File_List[File_List_Entry].split(',')
#         if len(Line_Parts[0]) > Max_Name_String:
#             Max_Name_String = len(Line_Parts[0])
#         File_List_Entry += 1
#     return Max_Name_String
#
#
# def Find_Location_String_Length(File_List):
#     File_List_Entry = 0
#
#     Max_Location_String = 0
#     for i in range(3):
#         Line_Parts = File_List[File_List_Entry].split(',')
#         if len(Line_Parts[1]) > Max_Location_String:
#             Max_Location_String = len(Line_Parts[1])
#         File_List_Entry += 1
#     return Max_Location_String
#
# Main()
#
# #
# def Extract(Places_List):
#     return [item[0] for item in Places_List]
#

# Display_File = open("places.csv")
# Total = 0
# for line in Display_File:
#     Total += 1
# print(Total)















Display_File = open("places.csv")
Places_List = []
for line in range(3):
    line = Display_File.readline().strip()
    Line_Parts = line.split(',')
    Line_Parts[2] = int(Line_Parts[2])
    Places_List.append(Line_Parts)

print(Places_List)
New_Row = 0
All_Visited = True
for i in range(3):
    if 'n' in Places_List[New_Row][-1]:
        All_Visited = False
    else:
        New_Row += 1
print(All_Visited)
# Row_In_List = 1
# New_Line_In_List = 0
# for i in range(3):
#     if Places_List[New_Line_In_List][3] == 'n':
#         Places_List.insert([New_Line_In_List][0][0], '*')
#
#
#         # print(
#         #     f" {Row_In_List}. {Places_List[New_Line_In_List][0]} in {Places_List[New_Line_In_List][1]} priority {Places_List[New_Line_In_List][2]}")
#     Row_In_List += 1
#     New_Line_In_List += 1
# print(Places_List[0])

# # # print(Extract(Places_List)[1])
# # Total_List_Items = 0
# # for i in Places_List:
# #     Total_List_Items += 1
# # print(Total_List_Items)
# print(len(Places_List))
# # File_List_Entry = 0
#
# Max_Name_String = 0
# for i in range(3):
#     print(f"Line parts: {Line_Parts}")
#     if len(Places_List[File_List_Entry][0]) > Max_Name_String:
#         Max_Name_String = len(Places_List[File_List_Entry][0])
#     File_List_Entry += 1
# print(Max_Name_String)


# def main():
#     Display_File = open("places.csv")
#     Places_List = []
#     for line in range(3):
#         line = Display_File.readline().strip()
#         Line_Parts = line.split(',')
#         Line_Parts[2] = int(Line_Parts[2])
#         Places_List.append(Line_Parts)
#     print(Places_List)
#     Total = 0
#     # In_List = False
#     # Priority_Input = int(input("Number?: "))
#     # for i in range(3):
#     #     if Priority_Input in Places_List[Total]:
#     #         In_List = True
#     #     else:
#     #         Total += 1
#     # print(In_List)
#
#
#
#     Number_Input = Error_Check_Priority_Input(Places_List)
#     print(Number_Input)
#
#
#
#
#
#
# def Check_Priority_In_List(Priority_Input, Places_List):
#
#     Input_In_List = False
#     total = 0
#     for i in range(3):
#         if Priority_Input in Places_List[total]:
#             Input_In_List = True
#
#         else:
#             total += 1
#     return Input_In_List
#
#
#
#
# def Error_Check_Priority_Input(Places_List):
#     valid_integer = False
#     while not valid_integer:
#         try:
#             Priority_Input = int(input("Number?: "))
#             if Priority_Input <= 0:
#                 print("Number must be > 0")
#             else:
#                 Input_In_List = Check_Priority_In_List(Priority_Input, Places_List)
#                 if Input_In_List == True:
#                     print("Invalid place number")
#                 else:
#                     valid_integer = True
#
#         except ValueError:
#             print("Invalid input; enter a valid number")
#     return Priority_Input

#     valid_integer = False
#     Input_In_List = False
#     while not Input_In_List:
#         while not valid_integer:
#
#             try:
#                 Priority_Input = int(input("Number?: "))
#                 if Priority_Input <= 0:
#                     print("Number must be > 0")
#                 else:
#                     valid_integer = True
#             except ValueError:
#                 print("Invalid input; enter a valid number")
#         Yes = Check_If_Input_In_List(Priority_Input, Places_List)
#         if Yes == False:
#             Input_In_List = True



# main()

# while not valid:
#         if Priority_Input in Places_List[Total]:
#             print("Invalid")
#             Priority_Input = int(input("Number?: "))
#             Total += 1
#         else:
#             print("Worked")
#             valid = True



# valid = False
# while not valid:
#     if Priority_Input < 0:
#         print("Invalid input; enter a valid number")
#     elif len(Priority_Input) == 0:
#         print("Can't be blank")
#     elif Priority_Input in Places_List:
#         print("That place is already visited")
#     else:
#         valid = True
# print(f"It worked: {Priority_Input}")

# print(Max_Location_String)
# print(Max_Name_String)
# print(Max_Location_String)
# print(len(Line_Parts[1]))

    # Name_Length = Max_Name_String_Length(Line_Parts)
    # Location_Length = Max_Location_String_Length(Line_Parts)
        # if len(Line_Parts[0]) > Max_Name_String:
        #     Max_Name_String = len(Line_Parts[0])
        # if len(Line_Parts[1]) > Max_Location_String:
        #     Max_Location_String = len(Line_Parts[1])
#     print(f"{Row_In_List}. {Line_Parts[0]:{Name_Length}} in {Line_Parts[1]:{Location_Length}} priority {Line_Parts[2]}")
#     Row_In_List += 1
#     File_List_Entry += 1
#
# print(Name_Length)
# print(Max_Location_String)




#     File_List.append(Line_Parts)
# print(File_List)
# line = line.strip(",")
# Line_Parts = line.split()
# print(Line_Parts[0])
# for line in Display_File:
    # line = line.strip(",")
    # Line_Parts = line.split()
    # print(Line_Parts)
    # File_List.append(Line_Parts)
# print(len(File_List))
# List_Total = 0
# print(File_List[0])
# Individual_List = []
# Individual_List.append(File_List[0])
# print(f"Individual list: {Individual_List}")


# for i in range(len(File_List)):
#     print(File_List[List_Total])
#     List_Total += 1






