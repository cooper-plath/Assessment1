
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

Display_File = open("places.csv")
File_List = []
for line in range(3):
    line = Display_File.readline().strip()
    File_List.append(line)
print(File_List)
Total = 0
Numbered_Line = 1
for i in range(3):
    Line_Parts = File_List[Total].split(',')
    Line_Parts[2] = int(Line_Parts[2])
    if Line_Parts[3] == 'n':
        print(f"*{Numbered_Line}. {Line_Parts[0]} in {Line_Parts[1]} priority {Line_Parts[2]}")
    else:
        print(f" {Numbered_Line}. {Line_Parts[0]} in {Line_Parts[1]} priority {Line_Parts[2]}")
    Numbered_Line += 1
    Total += 1


# if line[3] == 'n':
#     #         print(f"  *{Total}. {line[0]:10} in {line[1]:12} priority {line[2]:2}")
#     #     else:
#     #         print(f"   {Total}. {line[0]:10} in {line[1]:12} priority {line[2]:2}")









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






