from model_of_mine import *
import random
class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__list_map = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 2, 4],
            [4, 2, 0, 2]
    ]

    @property
    def list_map(self):
        return self.__list_map
    def __zero_to_end(self):
        for i in range(-1, -len(self.__list_merge)-1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)


    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
                    if self.__list_merge[i] == self.__list_merge[i+1]:
                        self.__list_merge[i] += self.__list_merge[i+1]
                        del self.__list_merge[i+1]
                        self.__list_merge.append(0)


    def __left_move(self):
        for r in self.__list_map:
            self.__list_merge = r
            self.__merge()


    def __right_move(self):
        for r in range(len(self.__list_map)):
            self.__list_merge = self.__list_map[r][::-1]
            self.__merge()
            self.__list_map[r] = self.__list_merge[::-1]

    def __transpose(self):
        for r in range(len(self.__list_map)-1):
            for c in range(r+1,len(self.__list_map)):
                self.__list_map[r][c], self.__list_map[c][r] = self.__list_map[c][r], self.__list_map[r][c]


    def __move_up(self):
        self.__transpose()
        self.__left_move()
        self.__transpose()

    def __move_down(self):
        self.__transpose()
        self.__right_move()
        self.__transpose()

    def move(self,dir):
        if dir == DirectionModel.UP:
            self.__move_up()
        elif dir == DirectionModel.DOWN:
            self.__move_down()
        elif dir == DirectionModel.LEFT:
            self.__left_move()
        elif dir == DirectionModel.RIGHT:
            self.__right_move()

    def generate_rand_number(self):

        list_empty_location = self.__get_empty_location()
        if len(list_empty_location) == 0:
            return
        tuple_loc = random.choice(list_empty_location)
        # if random.randint(1,10) == 1:
            # self.__list_map[loc[0]][loc[1]] = 4  # 索引写死了，效果能实现但不建议！
        #     self.__list_map[tuple_loc.r_index][tuple_loc.c_index] = 4
        # else:
        #     self.__list_map[tuple_loc.r_index][tuple_loc.c_index] = 2
        self.__list_map[tuple_loc.r_index][tuple_loc.c_index] = 4 if random.randint(1,10) == 1 else 2
        # 由于最后一个空位置也产生了随机数，故移除掉最后一个空位置，因为现在也不叫做空位置了！
        list_empty_location.remove(tuple_loc) #有没有此句不影响
    def __get_empty_location(self):
        list_empty_location = []
        for r in range(len(self.__list_map)):
            for c in range(len(self.__list_map)):
                if self.__list_map[r][c] == 0:
                    list_empty_location.append(Location(r, c))
        return list_empty_location

    def is_game_over(self): # 判定依据两个条件，有没有空位置or能不能合并
        if len(self.__get_empty_location()) > 0:
            return False
        else:
            for r in range(len(self.__list_map)):
                for c in range(len(self.__list_map)-1):
                    if self.__list_map[r][c] == self.__list_map[r][c+1] or self.__list_map[c][r] == self.__list_map[c+1][r]:
                        return False
            return True

g01 = GameCoreController()
# g01.move_down()
# print(g01.list_map)
# g01.move(3)
# g01.generate_rand_number()
g01.is_game_over()
# print(g01.list_map)
