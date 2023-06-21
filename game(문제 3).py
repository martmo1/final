import turtle as t
import time
import math

t.setup(500, 700) # 캔버스 크기 500 X 700
t.title("Ping Pong") # 제목
t.tracer(1)

pen_ball = t.Turtle() # ball를 움직일 거북이 생성
pen_ball.up() # 이동 흔적이 남지 않게 펜을 들어 올림
pen_ball.speed(0) # ball의 속도는 매우 빠르게

pen_bar = t.Turtle() # bar를 움직일 거북이 생성
pen_bar.up() # 이동 흔적이 남지 않게 펜을 들어 올림
pen_bar.speed(0) # bar의 속도는 매우 빠르게

shapes = ["bar.gif", "ball.gif"] # bar 와 ball의 gif이름이 담긴 리스트

for shape in shapes:
    t.register_shape(shape) # bar 와 ball를 하나의 모양으로 등록


class Sprite():
    
    ## 생성자: 스프라이트의 위치, 가로/세로 크기, 이미지 지정

    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    ## 스프라이트 메서드

    # 지정된 위치로 스프라이트 이동 후 도장 찍기
    def render_ball(self, pen_ball):
        pen_ball.goto(self.x, self.y)
        pen_ball.shape(self.image)
        pen_ball.stamp()

    def render_bar(self, pen_bar):
        pen_bar.goto(self.x, self.y)
        pen_bar.shape(self.image)
        pen_bar.stamp()


    def is_aabb_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)
    
bar = Sprite(0, -270, 128, 24, "bar.gif")
ball = Sprite(0, 0, 32, 32, "ball.gif")

def right(): # 오른쪽 방향으로 이동할 함수
  if bar.x < 200: # bar의 현재 위치가 200보다 작으면 
    bar.x += 15 # 오른쪽(거북이 기준 앞으로)15칸씩 이동
    bar.render_bar(pen_bar) # bar의 Sprite를 위치 이동하고 도장찍기
    t.update() # 화면 업데이트
    pen_bar.clear() # 스프라이트 이동흔적 삭제

def left(): # 왼쪽 방향으로 이동할 함수
  if bar.x > -200: # bar의 현재 위치가 -200보다 크면 
    bar.x -= 15 # 왼쪽(거북이 기준 뒤로) 15칸씩 이동
    bar.render_bar(pen_bar) # bar의 Sprite를 위치 이동하고 도장찍기
    t.update() # 화면 업데이트
    pen_bar.clear() # 스프라이트 이동흔적 삭제

t.listen() # 키를 작동 시키기 위한 포커스 설정(이벤트 처리)
t.onkeypress(right, "Right") # 오른쪽 방향키를 누르면 right함수 실행
t.onkeypress(left, "Left") # 왼쪽 방향키를 누르면 left함수 실행

ball_xspeed = 15 # x축으로 이동할 변수
ball_yspeed = 15 # y축으로 이동할 변수

game_on = True # 게임이 진행중을 가르킴
life = 3 # 목숨은 3개

t.up() # 이동흔적이 남지 않게 펜을 들어줌
t.hideturtle() # 거북이를 숨김
t.goto(0, 300) # 거북이를 x축은 0, y축은 300으로 이동
t.write(f"life : {life}", False, "center", ("", 20)) # 문구 life : 를 출력하고 현재 남아있는 life의 개수를 출력, 이동하지 않고 고정시킴(False), 중앙 배열, 글자 크기는 20

while game_on: # 게임이 진행중(game_on == True)일때
    ball.x = ball.x + ball_xspeed # 새로운 x축을 현재 공의 x축 위치와 x축 변수 5를 더한 변수
    ball.y = ball.y + ball_yspeed # 새로운 y축을 현재 공의 y축 위치와 y축 변수 5를 더한 변수
    ball.render_ball(pen_ball) # ball의 Sprite를 위치 이동하고 도장찍기
    t.update() # 화면 업데이트
    pen_ball.clear() # 스프라이트 이동흔적 삭제

    if ball.x > 240 or ball.x < -240: # 공의 현재 x축의 위치가 240보다 크거나 -240보다 작으면 (왼쪽벽과 오른쪽 벽에 닿았을때)
        ball_xspeed = -ball_xspeed # x축으로 이동할 변수 방향 변경

    if ball.y > 340: # 공의 현재 y축의 위치가 340보다 크면(천장에 닿았을때)
        ball_yspeed = -ball_yspeed # y축으로 이동할 변수 방향 변경

    if ball.y < -340: # 공의 현재 y축의 위치가 -340보다 작으면(아래로 떨어질 때)
        life -= 1 # 목숨을 한 개 차감
        t.clear() # 문구 초기화
        t.write(f"life : {life}", False, "center", ("", 20)) # 목숨의 개수가 변경된 것을 새로 입력
        time.sleep(0.5) # 준비할 시간으로 0.5초를 줌
        ball.x = 0 # ball를 x축으로 0으로 이동
        ball.y = 100 # ball를 y축으로 100으로 이동
        ball.render_ball(pen_ball) # ball의 Sprite를 위치 이동하고 도장찍기
        t.update() # 화면 업데이트
        pen_ball.clear() # 스프라이트 이동흔적 삭제
        ball_xspeed = -ball_xspeed # x축 방향이 바뀐것을 다시 원래 방향으로 바꿈
        ball_yspeed = -ball_yspeed # y축 방향이 바뀐것을 다시 원래 방향으로 바꿈

        if life == 0: # 목숨이 0이 되면
            game_on = False # 게임의 진행을 중단
            t.goto(0, 0) # 거북이를 x축으로 0, y축으로 0으로 이동
            t.write("Game Over", False, "center", ("", 20)) # 문구 Game Over를 출력, 이동하지 않고 고정시킴, 글자 크기는 20

    if bar.is_aabb_collision(ball): # bar와 ball 사이의 거리가 50보다 작고 ball의 현재 y축 위치가 -245보다 작으면
        ball_yspeed = -ball_yspeed # y축으로 이동할 변수 방향 변경
