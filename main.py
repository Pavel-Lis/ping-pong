from pygame import *
from random import randint
font.init()
font2 = font.Font(None, 50)
window = display.set_mode((700, 500))
window.fill((124, 252, 0))
display.set_caption('Пинг-Понг')
class GameSprite(sprite.Sprite):
    def __init__(self, namefile, player_x, player_y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(namefile), (width, height))
        self.namefile = namefile
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
        self.width = width
        self.height = height
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player_1(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 20:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 420:
            self.rect.y += self.speed
class Player_2(GameSprite):
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 20:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 420:
            self.rect.y += self.speed
goal_1 = 0
goal_2 = 0
class Enemy(GameSprite):
    def update_3(self):
        global goal_1
        global goal_2
        if sprite.collide_rect(ball, racket_1):
            self.direction_1 = 'right'
            corner_1 = randint(0, 1)
            if corner_1 == 0:
                self.direction_2 = 'up'
            if corner_1 == 1:
                self.direction_2 = 'down'
        if sprite.collide_rect(ball, racket_2):
            self.direction_1 = 'left'
            corner_2 = randint(0, 1)
            if corner_2 == 0:
                self.direction_2 = 'down'
            if corner_2 == 1:
                self.direction_2 = 'up'
        if self.rect.x <= 0:
            self.direction_1 = 'right'
            goal_1 += 1
        if self.rect.x >= 630:
            self.direction_1 = 'left'
            goal_2 += 1
        if self.direction_1 == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.y <= 0:
            self.direction_2 = 'down'
        if self.rect.y >= 430:
            self.direction_2 = 'up'
        if self.direction_2 == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
ball = Enemy('ball.png', 350, 250, 5, 65, 65)
ball.direction_1 = 'right'
ball.direction_2 = 'up'
racket_1 = Player_1('racket_1.png', 50, 350, 4, 65, 65)
racket_2 = Player_2('racket_2.png', 590, 50, 4, 65, 65)
text_win_1 = font2.render('Игрок 1 выйграл!', 1, (0, 0, 128))
text_win_2 = font2.render('Игрок 2 выйграл!', 1, (255, 0, 0))
game = True
clock = time.Clock()
while game:
    clock.tick(60)
    window.fill((124, 252, 0))
    racket_2.reset()
    racket_2.update_2()
    racket_1.reset()
    racket_1.update_1()
    ball.reset()
    ball.update_3()
    for i in event.get():
        if i.type == QUIT:
            game = False
    if goal_1 == 1:
        window.blit(text_win_1, (250, 250))
        ball.speed = 0
    if goal_2 == 1:
        window.blit(text_win_2, (250, 250))
        ball.speed = 0
    display.update()