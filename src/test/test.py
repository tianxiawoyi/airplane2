

import pygame
# import requests

# print(pygame.__file__)
# class A(object):
#     def __init__(self):
#         print("AAAAAAAAAAA")
#         self.speak();
#
#     def speak(self):
#         print("A-speak")
pygame.init()
# while True:
#     # keypress = pygame.key.get_pressed()
#     pass
print(pygame.K_RIGHT)

# class B(object):
#     def __init__(self ,name):
#         self.name = name
#         print("bbbbbbbbbbbb")
#         self.speak();
#
#     def speak(self):
#         print("B-speak")
#
#
# class C(A ,B):
#     def __init__(self):
#         print("cccccccccc")
#         self.speak();
#         super(self ,C).speak()
#
#
#     def speak(self):
#         print("C-speak")
#
#
#
# class Game(object):
#     topScore = 100
#
#     def __init__(self):
#         self.score = 10
#
#     @classmethod
#     def speak(cls):
#         print("fsgfsg %s" % cls.topScore)
#
#     def speak1(self):
#         print("fsgfsg %s" % Game  .topScore)
#
# # Game.speak()
# Game().speak1()
#
#
#
# class MusicPlayer(object):
#     instance = None
#     init_flag = False
#     def __new__(cls, *args, **kwargs):
#
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#
#         return cls.instance
#
#     def __init__(self):
#
#         if MusicPlayer.init_flag:
#             return
#
#         print("init 方法")
#         MusicPlayer.init_flag = True


#
# player1 = MusicPlayer()
# print(player1)
#
# player2 = MusicPlayer()
# print(player2)

# try:
#     num = int(input("请输入整数:"))
#     result = 8 /num
#     print(result)
# except ValueError:
#     print("值错误")
# except Exception as result:
#     print("未知错误:%s" % result)
# else:
#     print("尝试成功")
# finally:
#     print("-"*50)


# def demo():
#     pwd = input("请输入密码")
#     if len(pwd) >= 8:
#         return pwd
#     print("中东抛异常")
#     ex= Exception("密码长度小于0","dddddddddd")
#     raise ex

# print(demo() )

