import pygame
# import plane_sprite
from my_airplane.plane_sprite import *


class PlayGame(object):

    def __init__(self):
        print("初始化游戏...")

        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        # 创建精灵
        self.__creat_sprites()

        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)  # 设置定时器,敌机出现的时间 1s

        pygame.time.set_timer(HERO_FIRE_EVENT, 500)  # 设置定时器,英雄子弹发射时间 0.5


    def start_game(self):   # 开始游戏
        print("游戏开始...")

        while True:
            self.clock.tick(60)

            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __event_handler(self):  # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlayGame.game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                ens = EnemySprite()
                self.ens_group.add(ens)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed_x = 4
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed_x = -4
        else:
            self.hero.speed_x = 0

    def __creat_sprites(self):  # 创建精灵
        bg1 = BackGround()
        bg2 = BackGround(y=-SCREEN_RECT.height)
        self.bg_group = pygame.sprite.Group(bg1, bg2)

        ens = EnemySprite()
        self.ens_group = pygame.sprite.Group(ens)

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __check_collide(self):  # 碰撞检测

        # 子弹撞毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_group,self.ens_group,True,True)

        # 2. 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.ens_group, True)
        if len(enemies)>0:
            self.hero.kill()
            PlayGame.game_over()

    def __update_sprites(self):   # 更新精灵
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.ens_group.update()
        self.ens_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)


    @staticmethod
    def game_over():
        print("游戏结束...")
        pygame.quit()
        exit()




if __name__ == '__main__':
    PlayGame().start_game()
