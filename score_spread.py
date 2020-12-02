def spread():
    f = open("name_score.txt",'r')
    score = []
    while True:
        
        lines = f.readline()
        if not lines: break
        
        retry = lines.split("\n")
        if retry[0].isdigit():
    
            score.append(int(retry[0]))
    score.sort()
    score.reverse()
    for i in range(3):
        print("{} : {}".format(i+1,score[i]))
    f.close()
spread()
