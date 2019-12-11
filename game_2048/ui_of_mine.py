'''
２０４８界面显示
'''
from bll_of_mine import *  #被导入的模块不要有调用的语句
import os
class GameConsoleView:
    def __init__(self):
        self.__controller = GameCoreController()

    def main(self):
        self.__start()
        self.__update()

    def __start(self):
        self.__controller.generate_rand_number()
        self.__controller.generate_rand_number()
        self.__draw_map()
    def __draw_map(self):
        # 清空控制台
        os.system('clear')
        for line in self.__controller.list_map:
            for i in line:
                print(i,end=' ')
            print()


    def __update(self):
        while True:
            self.__move_direction()
            self.__controller.generate_rand_number()
            self.__draw_map()
            if self.__controller.is_game_over():
                print('游戏结束')
                break
    def __move_direction(self):
        dir = input('请输入(wasd)')
        # if dir == 'w':
        #     self.__controller.move(DirectionModel.UP)
        # elif dir == 's':
        #     self.__controller.move(DirectionModel.DOWN)
        # elif dir == 'a':
        #     self.__controller.move(DirectionModel.LEFT)
        # elif dir == 'd':
        #     self.__controller.move(DirectionModel.RIGHT)
        # 第二种
        dict_dir = {
            'w':DirectionModel.UP,
            's':DirectionModel.DOWN,
            'a':DirectionModel.LEFT,
            'd':DirectionModel.RIGHT
        }
        if dir in dict_dir:
            self.__controller.move(dict_dir[dir])


if __name__ == '__main__':
    viewer = GameConsoleView()
    viewer.main()



























#－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# 初始的！
# from bll import *
# class GameConsoleView:
#     def __init__(self):
#         self.__controller = GameCoreController()
#     def main(self):
#         self.__start()
#         self.update()
#     def __start(self):
#         self.__controller.generate_rand_number()
#         self.__controller.generate_rand_number()
#         self.__draw_map()
#     def __draw_map(self):
#         # os.system('clear')
#         for line in self.__controller.list02_target:
#             for i in line:
#                 print(i,end=' ')
#             print()
#
#     def update(self):
#         while True:
#             if input(' ') == 'W':
#                 self.__controller.move(DirectionModel.UP)
#                 self.__controller.generate_rand_number()
#                 self.__draw_map()
#                 if self.__controller.is_gameover():
#                     print('游戏结束')
#                 break
#             elif input(' ') == 'S':
#                 self.__controller.move(DirectionModel.DOWN)
#                 self.__controller.generate_rand_number()
#                 self.__draw_map()
#                 if self.__controller.is_gameover():
#                     print('游戏结束')
#                 break
#             elif input(' ') == 'A':
#                 self.__controller.move(DirectionModel.LEFT)
#                 self.__controller.generate_rand_number()
#                 self.__draw_map()
#                 if self.__controller.is_gameover():
#                     print('游戏结束')
#                 break
#             elif input(' ') == 'D':
#                 self.__controller.move(DirectionModel.RIGHT)
#                 self.__controller.generate_rand_number()
#                 self.__draw_map()
#                 if self.__controller.is_gameover():
#                     print('游戏结束')
#                 break
#
#
# if __name__ == '__main__':
#     viewer = GameConsoleView()
#     viewer.main()
#     viewer.update()