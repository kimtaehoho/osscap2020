
f = open("name_score.txt",'r')
score = []
while True:
        
    lines = f.readline()
    if not lines: break
    print(lines)
    retry = lines.split("\n")
    if retry[0].isdigit():
    
        score.append(retry[0])
print(score)
f.close()