import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)  # 屏幕大小

GAME_FRAME = 60  # 游戏刷新帧率

CREATE_ENEMY_EVENT = pygame.USEREVENT  # 创建敌机事件

HERO_FIRE_EVENT = pygame.USEREVENT + 1 # 英雄发射子弹事件


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, img_name, speed=1):
        super(GameSprite, self).__init__()
        self.image = pygame.image.load(img_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed  # 垂直yidong


class BackGround(GameSprite):

    def __init__(self, x=0, y=0):
        super(BackGround, self).__init__("./images/background.png")
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        super(BackGround, self).update()
        if self.rect.y >= SCREEN_RECT.height:
            # self.rect.y = -SCREEN_RECT.height
            self.rect.bottom = 0
            # SCREEN_RECT.bottom



class EnemySprite(GameSprite):

    def __init__(self):
        super(EnemySprite, self).__init__("./images/enemy1.png")
        self.rect.x = random.randint(0,SCREEN_RECT.right-self.rect.width)
        self.rect.bottom = 0

        self.x_speed = random.randint(0,2)    # 0~2的随机整数

    def update(self, *args):
        super(EnemySprite, self).update()

        self.rect.x += self.x_speed     # X方向随机(0,2)的速度
        if self.rect.right >= SCREEN_RECT.width or self.rect.left <= SCREEN_RECT.left:  # 到达左右两边方向相反
            self.x_speed= -self.x_speed
        elif self.rect.y >= SCREEN_RECT.height:
            self.kill()


    def __del__(self):
        print("敌机挂了... %s" % self.rect)
        pass



class Hero(GameSprite):

    def __init__(self):
        super(Hero, self).__init__("./images/life.png")
        self.speed = 0
        self.speed_x = 0
        self.rect.bottom = SCREEN_RECT.bottom-80
        self.rect.centerx = SCREEN_RECT.centerx
        self.bullet_group = pygame.sprite.Group()

    def fire(self):
        if self.bullet_group is None:
            self.bullet_group = pygame.sprite.Group()

        for i in range(0,3):
            # print("--------->%d" % i)
            bullet = Bullet(self.rect)
            bullet.rect.bottom = bullet.rect.bottom - i * (bullet.rect.height + 10)
            self.bullet_group.add(bullet)


    def update(self, *args):
        self.rect.x += self.speed_x
        if self.rect.right >= SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width
        elif self.rect.left <= SCREEN_RECT.left:
            self.rect.left = SCREEN_RECT.left




class Bullet(GameSprite):

    def __init__(self, sprite_rect:pygame.Rect, speed=-2):
        super(Bullet, self).__init__("./images/bullet1.png")
        self.speed = speed
        self.rect.centerx = sprite_rect.centerx
        self.rect.bottom = sprite_rect.top


    def update(self, *args):
        self.rect.y += self.speed

        if self.rect.bottom <= 0 or self.rect.top >= SCREEN_RECT.bottom:
            self.kill()


    def __del__(self):
        print("子弹消失...%s" % self.rect)