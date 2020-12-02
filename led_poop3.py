# -*- coding: utf-8 -*-
import score_spread
start = 'n'

t = open("names.txt",'a')
t.close()
t = open("names.txt",'r')
name_list = []
while True:
        
    lines = t.readline()
    if not lines: break
        
    retry = lines.split("\n")
    if retry[0].isalpha():
    
        name_list.append(retry[0])

while(1):
    start = input("계속 하시겠습니까?? (y/n)")
    print(name_list)
    if start == 'n':
        break
    answer = input("등록된 사용자입니까? (y/n)")
    if answer == "y":
        import cv2
        import numpy as np
        import os

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')
        cascadePath = "haarcascades/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath);
        font = cv2.FONT_HERSHEY_SIMPLEX

        #iniciate id counter
        id = 0
        
        # names related to ids: example ==> loze: id=1,  etc
        # 이런식으로 사용자의 이름을 사용자 수만큼 추가해준다.
        # names = ['NONE', 'kihun', 'dahyun', 'taeho', '???']

        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video widht
        cam.set(4, 480) # set video height

        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        while True:
            ret, img =cam.read()
            img = cv2.flip(img, -1) # Flip vertically
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
            faces = faceCascade.detectMultiScale( 
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
               )

            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                # Check if confidence is less them 100 ==> "0" is perfect match
                if (confidence < 100):
                    id = name_list[id]
                    confidence = "  {0}%".format(round(100 - confidence))
                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
            
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
            cv2.imshow('camera',img)
            
            if id in name_list:
                break
            
            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
            
        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()

        from matrix import *  # matrix.py의 모든 함수들 가져오기
        import time
        import random
        import pygame
        import pygame as pg
        import sys
        import LED_display as LMD
        import threading

        def LED_init():
            thread=threading.Thread(target=LMD.main, args=())
            thread.setDaemon(True)
            thread.start()
            return

        pg.init()
        screen = pg.display.set_mode((1, 1))

        def draw_matrix(m):
            array = m.get_array()  # matrix의 객체로 부터 array라는 리스트 생
            for y in range(m.get_dy()-4):  # y는 matrix의 각 행을 말함.
                for x in range(4, m.get_dx()-4):
                    if array[y][x] == 0:
                        LMD.set_pixel(x, 19-y, 0)
                    elif array[y][x] == 1:
                        LMD.set_pixel(x, 19-y, 1)
                    elif array[y][x] == 2:
                        LMD.set_pixel(x, 19-y, 2)
                    elif array[y][x] == 3:
                        LMD.set_pixel(x, 19-y, 3)
                    elif array[y][x] == 4:
                        LMD.set_pixel(x, 19-y, 4)
                    elif array[y][x] == 5:
                        LMD.set_pixel(x, 19-y, 5)
                    elif array[y][x] == 6:
                        LMD.set_pixel(x, 19-y, 6)
                    elif array[y][x] == 7:
                        LMD.set_pixel(x, 19-y, 7)
                print()


        #색 다르게 설정해야함.

        GameOver = [
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], 
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7 ,7, 7, 7],
            [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7],
            [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7 ,7 ,7 ,7],
            [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7 ,7 ,7 ,7],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7],
            [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,7 ,7 ,7 ,7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7 ,7 ,7 ,7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ,7 ,7 ,7 ,7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1 ,7 ,7 ,7 ,7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0 ,7 ,7 ,7 ,7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1 ,7 ,7 ,7 ,7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], 
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],]


        rand = random.randint(1, 5)
        def set_block(rand):
            if rand == 1:
                arrayBlk = [[1]] #enemy
            elif rand == 2:
                arrayBlk = [[1, 1]]
            elif rand == 3:
                arrayBlk = [[1, 1, 1]]
            elif rand == 4:
                arrayBlk = [[4, 4], [4, 4]]  # character
            return arrayBlk

        Rand=random.randint(1,5)
        def set_color(Rand):
            if Rand == 1:
                array2Blk = [[3, 3], [3, 3]]
            if Rand == 2:
                array2Blk = [[2, 2], [2, 2]]
            elif Rand == 3:
                array2Blk = [[5, 5], [5, 5]]
            elif Rand == 4:
                array2Blk = [[6, 6], [6, 6]]
            return array2Blk





        iScreenDy = 16  # 높이를 15칸으로 정의
        iScreenDx = 32 # 폭을 10칸으로 정의
        iScreenDw = 4

        character_top = 6  # 초록색으로 지정해야함. , 나오는 도형의 좌측상단의 좌표y=0
        character_left = 28  # 똥이 나오는 x좌표

        item_top = random.randrange(4, 19) # 파란색으로 지정해야함. item 초기 y값
        item_left = 4

        enemy_top = random.randrange(4, 19) # 빨간색으로 지정해야함. enemy 초기 y값
        enemy_left = 0

        enemy2_top = random.randrange(4, 19) # 빨간색으로 지정해야함. enemy 초기 y값
        enemy2_left = 1

        enemy3_top = random.randrange(4, 19) # 빨간색으로 지정해야함. enemy 초기 y값
        enemy3_left = 2

        gameover=False

        arrayScreen = [
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], 
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 0
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 2
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 4
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 6
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 8
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 10
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 12
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 14
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], 
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
        ]

        item_speed = 1
        enemy_speed = 1
        enemy2_speed = 1
        enemy3_speed = 1

        score=0

        rand = random.randrange(1, 4)
        enemyBlk = Matrix(set_block(rand))

        rand = random.randrange(1, 4)
        enemy2Blk = Matrix(set_block(rand))

        rand = random.randrange(1, 4)
        enemy3Blk = Matrix(set_block(rand))

        Rand = random.randrange(1, 5)
        itemBlk = Matrix(set_color(Rand))

        print("아이템을 6(=30점)개 먹을때 마다 속도가 빨라집니다!")
        time.sleep(2)
        LED_init()

        item_plus = 0
        enemy_plus = 0
        enemy2_plus = 0
        enemy3_plus = 0
        #item_speed = 1
        #enemy_speed = 1
        start_time = time.time()


        while True:
            iScreen = Matrix(arrayScreen)
            # iscreen(입력스크린)
            oScreen = Matrix(iScreen)
            # oscreen(출력스크린)
            charBlk = Matrix(set_block(4))

            chartempBlk = iScreen.clip(character_top, character_left, character_top + charBlk.get_dy(),
                                       character_left + charBlk.get_dx())
            chartempBlk = chartempBlk + charBlk
            oScreen.paste(chartempBlk, character_top, character_left)

            itemtempBlk = iScreen.clip(item_top, item_left, item_top + itemBlk.get_dy(), item_left + itemBlk.get_dx())
            itemtempBlk = itemtempBlk + itemBlk
            oScreen.paste(itemtempBlk, item_top, item_left)

            enemytempBlk = iScreen.clip(enemy_top, enemy_left, enemy_top + enemyBlk.get_dy(), enemy_left + enemyBlk.get_dx())
            enemytempBlk = enemytempBlk + enemyBlk
            oScreen.paste(enemytempBlk, enemy_top, enemy_left)
            draw_matrix(oScreen);print()

            enemy2tempBlk = iScreen.clip(enemy2_top, enemy2_left, enemy2_top + enemy2Blk.get_dy(), enemy2_left + enemy2Blk.get_dx())
            enemy2tempBlk = enemy2tempBlk + enemy2Blk
            oScreen.paste(enemy2tempBlk, enemy2_top, enemy2_left)
            draw_matrix(oScreen);print()

            enemy3tempBlk = iScreen.clip(enemy3_top, enemy3_left, enemy3_top + enemy3Blk.get_dy(), enemy3_left + enemy3Blk.get_dx())
            enemy3tempBlk = enemy3tempBlk + enemy3Blk
            oScreen.paste(enemy3tempBlk, enemy3_top, enemy3_left)
            draw_matrix(oScreen);print()

            item_plus = score//30
            enemy_plus = score//30
            enemy2_plus = score//30
            enemy3_plus = score//30

            #아이템과 똥이 떨어지는 것을 표현하기 위함.

            item_left  += 1 + item_plus
            enemy_left += 1 + enemy_plus
            enemy2_left += 1 + enemy2_plus
            enemy3_left += 1 + enemy3_plus

            gameover=False

            #스코어가 30점씩 늘어날때 마다 스피드가 빨라지게 하는 코드 작성해야함.

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        if character_top < 18:
                            character_top += 1
                    elif event.key == pg.K_RIGHT:
                        if character_top > 4:
                            character_top -= 1

            if enemytempBlk.anyGreaterThan(7):
                enemy_left = 2
                enemy_top = random.randrange(4, 19)
                rand=random.randrange(1,4)
                enemyBlk = Matrix(set_block(rand))

            if enemy2tempBlk.anyGreaterThan(7):
                enemy2_left = 3
                enemy2_top = random.randrange(4, 19)
                rand=random.randrange(1,4)
                enemy2Blk = Matrix(set_block(rand))

            if enemy3tempBlk.anyGreaterThan(7):
                enemy3_left = 4
                enemy3_top = random.randrange(4, 19)
                rand=random.randrange(1,4)
                enemy3Blk = Matrix(set_block(rand))

            if itemtempBlk.anyGreaterThan(7):
                item_left = 1
                item_top = random.randrange(4, 19)  # 파란색으로 지정해야함
                while(enemy_top-1 <= item_top <= enemy_top+1):
                    item_top = random.randrange(4,19)


            if item_plus < 4:
                if item_left == 25 :
                    if character_top-2<=item_top<=character_top+1:
                        score+=5
                        Rand = random.randrange(1, 5)
                        itemBlk = Matrix(set_color(Rand))
                        while (enemy_top - 1 <= item_top <= enemy_top + 2):
                            item_left = 1
                            item_top = random.randrange(4, 19)

            elif item_plus >= 4:
                if item_left >= 25 :
                    if character_top-2<=item_top<=character_top+1:
                        score+=5
                        Rand = random.randrange(1, 5)
                        itemBlk = Matrix(set_color(Rand))
                        while (enemy_top - 1 <= item_top <= enemy_top + 2):
                            item_left = 1
                            item_top = random.randrange(4, 19)

            if 27 < enemy_left :
                if character_top  <= enemy_top <= character_top + 1:
                    gameover=True
                    break

            if 27 < enemy2_left :
                if character_top  <= enemy2_top <= character_top + 1:
                    gameover=True
                    break

            if 27 < enemy3_left :
                if character_top  <= enemy3_top <= character_top + 1:
                    gameover=True
                    break

            print(score)
            time.sleep(0.1)

        if gameover == True:
            gameoScreen = Matrix(GameOver)
            draw_matrix(gameoScreen);print()
            print(score)
            time.sleep(2)
            f = open("name_score.txt",'a')
            f.write('\n')
            f.write(str(score))
            f.close()

       
        print(id,": ",score)
        score_spread.spread()
        #f = open("name_score.txt",'r')
        #f.close()
        #names = ['NONE', 'kihun', 'dahyun', 'taeho', '???']

    elif answer == "n":
        import cv2
        import os

        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video width
        cam.set(4, 480) # set video height
        face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

        # For each person, enter one numeric face id
        n = input("put your name first")
        name_list.append(n)
        t = open("names.txt",'a')
        t.writelines('%s\n' % n)
        face_id = input('\n enter user id = {} end press <return> ==>  '.format(len(name_list)-1))
        
        print("\n [INFO] Initializing face capture. Look the camera and wait ...")

        # Initialize individual sampling face count
        count = 0
        while(True):
            ret, img = cam.read()
            #img = cv2.flip(img, -1) # flip video image vertically
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
                count += 1
                # Save the captured image into the datasets folder
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
                cv2.imshow('image', img)
            k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
            elif count >= 30: # Take 30 face sample and stop video
                 break
        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()

        import cv2
        import numpy as np
        from PIL import Image
        import os

        # Path for face image database
        path = 'dataset'
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        detector = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml");

        # function to get the images and label data
        def getImagesAndLabels(path):
            imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
            faceSamples=[]
            ids = []
            for imagePath in imagePaths:
                PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
                img_numpy = np.array(PIL_img,'uint8')
                id = int(os.path.split(imagePath)[-1].split(".")[1])
                faces = detector.detectMultiScale(img_numpy)
                for (x,y,w,h) in faces:
                    faceSamples.append(img_numpy[y:y+h,x:x+w])
                    ids.append(id)
            return faceSamples,ids
        print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
        faces,ids = getImagesAndLabels(path)
        recognizer.train(faces, np.array(ids))

        # Save the model into trainer/trainer.yml
        recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi
        # Print the numer of faces trained and end program
        print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
        continue
t.close() 
