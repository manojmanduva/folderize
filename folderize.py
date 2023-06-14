import os
import tkinter as tk
from tkinter import filedialog
import shutil
import subprocess


basepath = filedialog.askdirectory()
#basepath = '/Users/manojvmanduva/Documents/Manoj/General/Images'
list=[]
files=[]

with os.scandir(basepath) as entries:
    for entry in entries:
        #creating extension from the filenames
        if os.path.isfile(entry):
            ext = os.path.splitext(entry)[1]
            #cleaning the extension
            cext = ext.rsplit(".",1)[-1]
            #removing redundant file types
            list.append(cext)
        
            file_types = set(list)
            path = basepath + '/' + cext
            if not entry.name.startswith('.') :
                file=entry.name
                files.append(file)
        else:
            print('No files exist')
            tk.simpledialog.askfloat('No Files Exist')
            break
    
    
for item in file_types:
    new_path = basepath+'/'+'Subfolder_'+item
    new_folder = os.mkdir(new_path)
    #new_folder = os.mkdir(basepath+'/'+'Subfolder_'+item)
    #new_folder = os.mkdir(basepath+'/'+'Subfolder_'+item)
    for file in files:
        if file.rsplit(".",1)[-1] == item :
            print(item)
            print(file)
            print(new_path)
            shutil.copy(basepath+'/'+file,new_path)
        
os.path.realpath(basepath)
            
