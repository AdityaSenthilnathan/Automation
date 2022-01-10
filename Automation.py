import os
import sys
#Program deletes duplicate files given a folder

folder  = input("Write the path of the file")

for root, dirs, files in os.walk(folder):
     print("in")
     
     for file in files:
         f = file
         for f2 in files:
             file1 = root + "/" + f
             file2 = root + "/" + f2
             if(file1 != file2):                   
                if os.path.exists(file1):
                    if os.path.exists(file2):       
                    
                    
                        with open(file1, 'rb') as a:
                            file1Read = a.read()
                        with open(file2, 'rb') as b:
                            file2Read = b.read()
                        
                        
                        
                    
                        if os.path.exists(file2):     
                            if file2Read == file1Read:
                                print( file1 + "same" + file2)
                                os.remove(file2)
                            else:
                                print("not same")
                        
