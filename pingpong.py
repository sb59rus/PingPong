from pygame import *
from random import randint
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, w, h, player_x, player_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.speed_x = self.speed
        self.speed_y = int(self.speed/2)
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y>0:
            self.rect.y-=self.speed 
        if key_pressed[K_s] and self.rect.y<450:
            self.rect.y+=self.speed 

class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y>0:
            self.rect.y-=self.speed 
        if key_pressed[K_DOWN] and self.rect.y<450:
            self.rect.y+=self.speed 

class Ball(GameSprite):
    def update(self):
        global score1
        global score2
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.y<1 or self.rect.y>549:
            self.speed_y*=-1
        if sprite.collide_rect(ball, raker1) or sprite.collide_rect(ball, raker2):
            self.speed_x*=-1
        if self.rect.x<1:
            score2+=1
            self.rect.x = 575
            self.rect.y = 275
        if self.rect.x>1199:
            score1+=1
            self.rect.x = 575
            self.rect.y = 275

#Игровая сцена:
bg = (194, 194, 214)
score_color = (51, 51, 51)
window = display.set_mode((1200, 600))
display.set_caption("PingPong")
window.fill(bg)

#переменные
finish = False
run = True
clock = time.Clock()
raket_image = 'raket.png'
ball_image = 'ball.png'
score1 = 0
score2 = 0
text_size = 250

#создание спрайтов
raker1 = Player1(raket_image, 15, 150, 10, 250, 5)
raker2 = Player2(raket_image, 15, 150, 1175, 250, 5)
ball = Ball(ball_image, 50, 50, 575, 275, 7)

#музыка
mixer.init()
mixer.music.load('Minimal.ogg')
mixer.music.play()

#шрифты
font.init()

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill(bg)

    player1_score = font.SysFont('Arial', text_size).render(str(score1), 1, score_color)
    player2_score = font.SysFont('Arial', text_size).render(str(score2), 1, score_color)
    window.blit(player1_score,(100,175))
    window.blit(player2_score,(975,175))

    if not(finish):
        raker1.update()
        raker1.reset()
        raker2.update()
        raker2.reset()
        ball.update()
        ball.reset()

        if score1 == 10:
            finish = True
            text_size = 70
            score1 = 'WIN'
            score2 = 'LOSE'
        if score2 == 10:
            finish = True
            text_size = 70
            score1 = 'LOSE'
            score2 = 'WIN'
    display.update()
    clock.tick(60)