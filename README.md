# osscap2020

-------------프로그램 설치 및 사용법---------------------
1. picamera 라즈베리 파이에 연결 및 세팅
참고 링크: https://inmile.tistory.com/17#:~:text=*%20%EC%B9%B4%EB%A9%94%EB%9D%BC%EB%A5%BC%20%EC%97%B0%EA%B2%B0%ED%95%A0%20%EB%95%8C%EB%8A%94%20%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC,%EB%81%88%20%EC%83%81%ED%83%9C%EC%97%90%EC%84%9C%20%EC%A7%84%ED%96%89%ED%95%9C%EB%8B%A4.&text=%ED%94%8C%EB%9E%AB%20%EC%BC%80%EC%9D%B4%EB%B8%94%20%ED%98%95%ED%83%9C%EB%A1%9C%20%EA%B5%AC%EC%84%B1,%EC%88%98%20%EC%9E%88%EB%8A%94%20%EC%83%81%ED%83%9C%EB%A1%9C%20%EB%A7%8C%EB%93%A0%EB%8B%A4

1) picamera를 raspberry3에 연결

2) terminal에서 Update 진행

$ sudo apt-get update
$ sudo apt-get upgrade

3) terminal에서 카메라 enable

$ sudo raspi-config

interface option -> camera 들어가서 enable 하시겠습니까? 가 뜨면 yes 설정 후 닫기

2. opencv 설치(python은 이미 설치됨을 전제)

** 정석대로 설치 시 build에 너무 오랜 시간이 걸리고, raspberry 과열로 오류가 떠서 이미 build된 파일이 있는 파일을 이용하여 설치하였습니다 **

참고 링크:
https://blog.xcoda.net/97

1) opencv를 설치할 디렉토리를 생성 후,
mkdir openCV
cd openCV

2) 다음 명령어를 차례로 시행합니다.
sudo apt-get update
wget https://github.com/dltpdn/opencv-for-rpi/releases/download/4.2.0_buster_pi3b/opencv4.2.0.deb.tar
tar -xvf opencv4.2.0.deb.tar
sudo apt-get install -y ./OpenCV*.deb
pkg-config --modversion opencv4

3) python3 명령어 입력 후 opencv 설치 확인
import cv2
cv2.__version__

4) 설치 완료

3. 프로젝트 실행
$ git clone https://github.com/kimtaehoho/osscap2020.git
$ cd cam/
$ python3 face_rec_game.py

4. 프로젝트 설명
처음 소스코드를 실행하면
계속하시겠습니까?? 문구가 뜹니다.
y를 누르면 실행

등록된 사용자입니까?

등록된 사용자면 y 입력

-> 화면이 뜨고 카메라에 얼굴을 인식시키면 인식되자마자 게임 실행

등록되지 않은 사용자면 n 입력

-> id를 입력하라고 뜹니다. 예시)put your name first:dahyun

-> enter user id = {?} end press <return> ==>  라는 명령어가 뜨면 입력하라는 숫자를 입력해줍니다.(정수 아이디) 예시)enter user id = 1 end press <return> ==> 1
  
-> "[INFO] Initializing face capture. Look the camera and wait ..."

-> 문구와 함께 모니터에 화면이 뜨면 카메라 앞을 정면으로 바라봐줍니다 멈춰서 가까이 바라보고, 마스크를 벗어야 학습이 더 잘 됩니다 그리고 카메라를 살짝씩 상하좌우로 움직여줍니다. 

  그럼 몇 초 뒤 화면이 종료, 학습이 완료됩니다.
  
->  [INFO] Exiting Program and cleanup stuff"

->  [INFO] Training faces. It will take a few seconds. Wait ...

->  [INFO] {0} faces trained. Exiting Program"

-> 위 세 문장이 출력 완료되면 성공적으로 종료.

이후 처음 출력 화면으로 돌아갑니다.

<게임 설명>

게임은 키보드 왼쪽 오른쪽 화살표를 눌러 합니다.

빨간색 테트리스 블럭(enemy)에 맞으면 게임 종료,

여러가지 색으로 내려오는 2x2 박스모양 아이템을 먹으면 점수가 5점씩 추가됩니다.

이 때, 점수가 30점 이상이 되면 아이템과 enemy가 내려오는 속도가 빨라집니다.

게임이 종료되면 terminal 화면에 인식했던 사용자명과 점수가 뜹니다. 그리고 1 2 3등까지의 점수도 함께 출력됩니다!
