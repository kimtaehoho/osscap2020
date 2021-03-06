from matrix import *  # matrix.py의 모든 함수들 가져오기
import time
import random
import pygame
import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((1, 1))

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] >= 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()

GameOver = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]


rand = random.randint(1, 6)
def set_block(rand):
    if rand == 1:
        arrayBlk = [[1,1,1],[1,0,1],[1,1,1]] #enemy
    elif rand == 2:
        arrayBlk = [[1,1,1],[0,0,1],[1,1,1]]
    elif rand == 3:
        arrayBlk = [[0,0,1],[1,1,1],[0,0,1]]
    elif rand == 4:
        arrayBlk = [[0,0,1],[0,1,1],[1,1,1]]
    elif rand == 5:
        arrayBlk = [[1,1,1],[0,0,1],[0,1,1]]
    elif rand == 6:
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





iScreenDy = 12  # 높이를 15칸으로 정의
iScreenDx = 26  # 폭을 10칸으로 정의

character_top = 6  # 초록색으로 지정해야함. , 나오는 도형의 좌측상단의 좌표y=0
character_left = 24  # 똥이 나오는 x좌표

item_top = 4 # 파란색으로 지정해야함. item 초기 y값
item_left = 0

enemy_top = 9  # 빨간색으로 지정해야함. enemy 초기 y값
enemy_left = 0



gameover=False

arrayScreen = [
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],  # 0
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],  # 12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7],
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],  # 14
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
]

item_speed = 1
enemy_speed = 1

score=0

rand = random.randrange(1, 5)
enemyBlk = Matrix(set_block(rand))

Rand = random.randrange(1, 5)
itemBlk = Matrix(set_color(Rand))

print("아이템을 6(=30점)개 먹을때 마다 속도가 빨라집니다!")
time.sleep(2)

while True:
    iScreen = Matrix(arrayScreen)
    # iscreen(입력스크린)
    oScreen = Matrix(iScreen)
    # oscreen(출력스크린)
    charBlk = Matrix(set_block(6))


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


    #아이템과 똥이 떨어지는 것을 표현하기 위함.
    item_left += 1
    enemy_left += 1

    item_speed = 1
    enemy_speed = 1

    gameover=False

    #스코어가 30점씩 늘어날때 마다 스피드가 빨라지게 하는 코드 작성해야함.
    if score // 5:
        enemy_left += enemy_speed
        item_left += item_speed

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                character_top += 1
            elif event.key == pg.K_RIGHT:
                character_top -= 1
    if enemytempBlk.anyGreaterThan(7):
        enemy_left = 2
        enemy_top = random.randrange(4, 11)
        rand=random.randrange(1,5)
        enemyBlk = Matrix(set_block(rand))

    if itemtempBlk.anyGreaterThan(7):
        item_left = 1
        item_top = random.randrange(3, 12)  # 파란색으로 지정해야함
        while(enemy_top-1 <= item_top <= enemy_top+2):
            item_top = random.randrange(3,12)

    if item_left==25:
        if character_top-2<=item_top<=character_top+1:
            score+=5
            Rand = random.randrange(1, 5)
            itemBlk = Matrix(set_color(Rand))
            while (enemy_top - 1 <= item_top <= enemy_top + 2):
                item_left = 1
                item_top = random.randrange(3, 12)

    if 23 <= enemy_left <= 25:
        if character_top - 2 <= enemy_top <= character_top + 1:
            gameover=True
            break

    if character_top==1 or character_top==13:
        gameover = True
        break
    time.sleep(0.3)

if gameover == True:
    gameoScreen = Matrix(GameOver)
    draw_matrix(gameoScreen);print()
    time.sleep(2)
print(score)
