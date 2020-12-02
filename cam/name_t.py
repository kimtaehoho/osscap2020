name_txt = open("names.txt",'a')

name_list = []
while True:
        
    lines = name_txt.readline()
    if not lines: break
        
    retry = lines.split("\n")
    if retry[0].isalpha():
    
        name_list.append(retry[0])
name_txt.close()