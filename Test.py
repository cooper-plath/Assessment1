
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


def Main():
    Display_File = open("places.csv")
    File_List = []
    for line in range(3):
        line = Display_File.readline().strip()
        File_List.append(line)
    Name_Length = Find_Name_String_Length(File_List)
    Location_Length = Find_Location_String_Length(File_List)
    Row_In_List = 1
    Split_Line = 0
    for a in range(3):
        Line_Parts = File_List[Split_Line].split(',')
        Line_Parts[2] = int(Line_Parts[2])
        print(
            f"{Row_In_List}. {Line_Parts[0]:{Name_Length}} in {Line_Parts[1]:{Location_Length}} priority {Line_Parts[2]}")
        Split_Line += 1
        Row_In_List += 1



def Find_Name_String_Length(File_List):
    File_List_Entry = 0

    Max_Name_String = 0
    for i in range(3):
        Line_Parts = File_List[File_List_Entry].split(',')
        if len(Line_Parts[0]) > Max_Name_String:
            Max_Name_String = len(Line_Parts[0])
        File_List_Entry += 1
    return Max_Name_String


def Find_Location_String_Length(File_List):
    File_List_Entry = 0

    Max_Location_String = 0
    for i in range(3):
        Line_Parts = File_List[File_List_Entry].split(',')
        if len(Line_Parts[1]) > Max_Location_String:
            Max_Location_String = len(Line_Parts[1])
        File_List_Entry += 1
    return Max_Location_String

Main()









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






