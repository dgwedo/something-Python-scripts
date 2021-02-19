import os

# MANUAL
####################################################################################
# input_string = input("enter sub_folders need remove file : ")

# dir = "D:\\All\\Cisco CCNA 200-301\\NSTH-Cisco.CCNA.200-301.Exam.Part1\\" + input_string

# arr = os.listdir(dir)

# for i in arr:
#     if("it.srt" in i or "th.srt" in i or "pl.srt" in i or "ro.srt" in i or "id.srt" in i):
#         os.remove(dir + "\\" + i)
# print()
####################################################################################


# AUTO
####################################################################################
dir = "D:\\All\\Cisco CCNA 200-301\\NSTH-Cisco.CCNA.200-301.Exam.Part1"

arr = os.listdir(dir)

for folders in arr:
    sub_dir = dir + "\\" + folders
    # print(sub_dir)
    arr_1 = os.listdir(sub_dir)
    for files in arr_1:
        # print(files)
        if("it.srt" in files or "th.srt" in files or "pl.srt" in files or "ro.srt" in files or "id.srt" in files):
            print(dir + "\\" + folders + "\\" + files)
            os.remove(dir + "\\" + folders + "\\" + files)
print()
print("SUCCESS!!!")
####################################################################################
