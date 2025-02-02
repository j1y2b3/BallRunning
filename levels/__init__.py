import os
import re
from importlib import import_module

import data
import path

import level
'''
level_file_judge=lambda file_name:len(os.path.splitext(file_name)[0])==7 and os.path.splitext(file_name)[1]=='.py' and os.path.splitext(file_name)[0][0:5]=='level'
levels_name_list=[os.path.splitext(file_name)[0] for file_name in os.listdir(f'{path.path}\\levels\\') if level_file_judge(file_name)]
'''
level_name_pattern=re.compile(r'^level\d{2}\.py$')
files_list=os.listdir(f'{path.path}\\levels\\')
level_file_judge=lambda file_name:re.match(level_name_pattern,file_name)!=None

levels_name_list=[file_name[:7] for file_name in files_list if level_file_judge(file_name)]
levels_list=[]

for level_name in levels_name_list:
    import_module("."+level_name,__package__)
    levels_list.append(eval(f'{level_name}.create_level'))

data.levels_num=len(levels_list)

del level_name_pattern,files_list,level_file_judge,level_name
