import data

for level_name in data.levels_list:
    exec('from levels import %s'%level_name)

del level_name
