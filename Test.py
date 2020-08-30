#
# File_List = []
# Display_File = open("places.csv", "r")
# File = Display_File.read().split()
# File_List.append(File)
# print(len(File_List))


Display_File = open("places.csv", "r")
Total = 0
for i in Display_File:
    #
    Total += 1

print(Total)


    # return File
    # File_List = []
    # File_List.append(Display_File)
    # # File_Read = Display_File.read()
    # return File_List