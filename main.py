import glob
import os

class PRACTICE:

    def __init__(self):
        return

    def Get_File_List1(self, path):

        FilePath = "FilePath!!"
        FileName = "FileName!!"

        return FilePath, FileName

path = "" 
instance = PRACTICE()
print(instance.Get_File_List1(path))     # 에러 발생 지점, 괄호가 하나 빠져있음
