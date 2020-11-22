import pygame
from random import *

#############################################################
# 기본 초기화 ( 반드시 해야 하는 것들 )
pygame.init()  # 초기화

# 화면크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면타이틀 설정
pygame.display.set_caption("Avoid Poop")  # 게임이름

# FPS
clock = pygame.time.Clock()
#############################################################

# 1. 사용자 게임 초기화 ( 배경화면, 게임 이미지, 좌표, 속도, 폰트 .. )

background = pygame.image.load(r"C:\Users\hyund\background.png")
sprite = pygame.image.load(r"C:\Users\hyund\sprite.png")
#score점수 내려오는거 먹어야함 
score = pygame.image.load(r"C:\Users\hyund\score.png")
score_size = score.get_rect().size  # 이미지의 크기를 구해옴
score_width = score_size[0]
score_height = score_size[1]
score_x_pos = randint(0, screen_width - score_width)
score_y_pos = 0
score_speed = 0.2

score_list = []

##여기까찌 
sprite_size = sprite.get_rect().size
sprite_width = sprite_size[0]
sprite_height = sprite_size[1]
sprite_x_pos = 0
sprite_y_pos = screen_height - sprite_height

# 이동할 좌표
to_x = 0

# 이동속도
sprite_speed = 0.5

poop1 = pygame.image.load(r"C:\Users\hyund\poop1.png")
poop1_size = poop1.get_rect().size  # 이미지의 크기를 구해옴
poop1_width = poop1_size[0]
poop1_height = poop1_size[1]
poop1_x_pos = randint(0, screen_width - poop1_width)
poop1_y_pos = 0
poop1_speed = 0.5

poop2 = pygame.image.load(r"C:\Users\hyund\poop2.png")
poop2_size = poop2.get_rect().size  # 이미지의 크기를 구해옴
poop2_width = poop2_size[0]
poop2_height = poop2_size[1]
poop2_x_pos = randint(0, screen_width - poop2_width)
poop2_y_pos = 0
poop2_speed = 0.3

poop3 = pygame.image.load(r"C:\Users\hyund\poop3.png")
poop3_size = poop3.get_rect().size  # 이미지의 크기를 구해옴
poop3_width = poop3_size[0]
poop3_height = poop3_size[1]
poop3_x_pos = randint(0, screen_width - poop3_width)
poop3_y_pos = 0
poop3_speed = 0.1

score_font = pygame.font.Font(None,50)
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성(폰트,크기), None = 디폴트 폰트

#총시간
total_time = 0
total_score = 1
total_score += total_time
#시작시간
start_ticks = pygame.time.get_ticks() #현재 틱 받아오
# 경과 시간 계산
elapsed_time = (pygame.time.get_ticks() + start_ticks) / 1000 # 경과 시간(ms)을 1000으로 나눠 초 단위로 표시
running = True  # 게임의 진행 여부
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정(30)

    # 2. 이벤트 처리 ( 키보드, 마우스 .. )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트
            running = False
        if event.type == pygame.KEYDOWN:  # 키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= sprite_speed
            elif event.key == pygame.K_RIGHT:
                to_x += sprite_speed
        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    sprite_x_pos += to_x * dt
    poop1_y_pos += poop1_speed * dt
    poop2_y_pos += poop2_speed * dt
    poop3_y_pos += poop3_speed * dt
    score_y_pos += score_speed * dt
    
    if poop1_y_pos > screen_height:
        poop1_x_pos = randint(0, screen_width - poop1_width)
        poop1_y_pos = 0
    if poop2_y_pos > screen_height:
        poop2_x_pos = randint(0, screen_width - poop2_width)
        poop2_y_pos = 0
    if poop3_y_pos > screen_height:
        poop3_x_pos = randint(0, screen_width - poop3_width)
        poop3_y_pos = 0
    if score_y_pos > screen_height:
        score_x_pos = randint(0, screen_width - score_width)
        score_y_pos = 0
        
    # 가로 경계값 처리
    if sprite_x_pos < 0:
        sprite_x_pos = 0
    elif sprite_x_pos > screen_width - sprite_width:
        sprite_x_pos = screen_width - sprite_width

    # 4. 충돌 처리
    sprite_rect = sprite.get_rect()
    sprite_rect.left = sprite_x_pos
    sprite_rect.top = sprite_y_pos

    poop1_rect = poop1.get_rect()
    poop1_rect.left = poop1_x_pos
    poop1_rect.top = poop1_y_pos

    poop2_rect = poop2.get_rect()
    poop2_rect.left = poop2_x_pos
    poop2_rect.top = poop2_y_pos

    poop3_rect = poop3.get_rect()
    poop3_rect.left = poop3_x_pos
    poop3_rect.top = poop3_y_pos

    score_rect = score.get_rect()
    score_rect.left = score_x_pos
    score_rect.top = score_y_pos

    # 충돌 체크
    if poop1_rect.colliderect(sprite_rect):# 사각형기준으로 충돌이 있는지 확인하는 함수
        
        running = False
        if total_time + elapsed_time > 20 and poop2_rect.colliderect(sprite_rect):
            
            running = False
            if total_time + elapsed_time > 30 and poop3_rect.colliderect(sprite_rect):
                
                running = False
        
    if score_rect.colliderect(sprite_rect):##점수추가하는기능
        total_score += 5
        score_y_pos = 9000000
        print("!!")
        
    
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(sprite, (sprite_x_pos, sprite_y_pos))
    screen.blit(poop1, (poop1_x_pos, poop1_y_pos))
    if total_time + elapsed_time > 20:
        screen.blit(poop2, (poop2_x_pos, poop2_y_pos))
        if total_time + elapsed_time > 30:
            screen.blit(poop3, (poop3_x_pos, poop3_y_pos))
            
    screen.blit(score,(score_x_pos,score_y_pos))
    
    #screen.blit(game_over, (screen_width / 2, screen_height / 2))
    score_paste = score_font.render(str(total_score), True, (255,255,255)) # 출력할 글자, True, 글자 색상
    screen.blit(score_paste, (10,40)) # 화면에 점수가 그려지는 위치
    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() + start_ticks) / 1000 # 경과 시간(ms)을 1000으로 나눠 초 단위로 표시

    timer = game_font.render(str(int(total_time + elapsed_time)), True, (200,200,200)) # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10,10)) # 화면에 타이머가 그려지는 위치

    if not running:
        print("Running time: %d" %int(total_time + elapsed_time))
        print("Total Score : %d "%int(total_score))
        score_list.append(total_score)
        print(score_list)
    """if total_time - elapsed_time <= 0:
        print("TIME OUT")
        running = False"""#게임초를 시간설정하고 뻇을경우 게임종료하는것 필요할수도있어서 냄겨둡니당~..feat기르
    start_speed = 0.0001
    
    pygame.display.update()  # 게임화면을 계속 그리기
    if (total_time + elapsed_time)%15==0:##속도 15초마다 높일려고했는데 왜안돼 시밤바  이거 
        start_speed = start_speed *10
    poop1_speed += start_speed
    poop2_speed += start_speed
    poop3_speed += start_speed
    score_speed += start_speed
    pygame.display.update()
pygame.display.update()  # 게임화면을 계속 그리기
pygame.time.delay(2000)  # 2초 정도 대기 (2000ms)
pygame.quit()
