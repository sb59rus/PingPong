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
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.y<1 or self.rect.y>549:
            self.speed_y*=-1
        if sprite.collide_rect(ball, raker1) or sprite.collide_rect(ball, raker2):
            self.speed_x*=-1
        if self.rect.x<1 or self.rect.x>1199:
            self.rect.x = 575
            self.rect.y = 275

#Игровая сцена:
bg = (randint(0,255), randint(0,255), randint(0,255))
score_color = (randint(0,255), randint(0,255), randint(0,255))
window = display.set_mode((1200, 600))
display.set_caption("PingPong")
window.fill(bg)

#переменные
finish = False
run = True
clock = time.Clock()
raket_image = 'raket.png'
ball_image = 'ball.png'

#создание спрайтов
raker1 = Player1(raket_image, 15, 150, 10, 250, 5)
raker2 = Player2(raket_image, 15, 150, 1175, 250, 5)
ball = Ball(ball_image, 50, 50, 575, 275, 7)

#музыка
'''mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
shot = mixer.Sound('fire.ogg')'''

#шрифты
font.init()
player1_score = font.SysFont('Arial', 250).render('0', 1, score_color)
player2_score = font.SysFont('Arial', 250).render('0', 1, score_color)
'''win = font.SysFont('Arial', 70).render('YOU WIN', 1, (0,255,0))
lose = font.SysFont('Arial', 70).render('YOU WIN', 1, (0,255,0))'''

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill(bg)
    window.blit(player1_score,(100,175))
    window.blit(player1_score,(975,175))

    if not(finish):
        raker1.update()
        raker1.reset()
        raker2.update()
        raker2.reset()
        ball.update()
        ball.reset()

    display.update()
    clock.tick(60)