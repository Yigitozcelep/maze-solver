#https://www.codewars.com/kata/5b86a6d7a4dcc13cd900000b/python answer of this question

def maze_solver(ar):
    current = 0
    x_limit = len(ar)
    y_limit = len(ar[0])
    all_player = set()
    class Player:
        def __init__(self, x, y, answer):
            self.x = x
            self.y = y
            self.answer = answer
            all_player.add(self)

        def move(self):
            pos = "NESW"
            moves = [(self.x - 1, self.y),  # Nort
                     (self.x, self.y + 1),  # East
                     (self.x + 1, self.y),  # South
                     (self.x, self.y - 1)]  # West
            for position,move in enumerate(moves):
                x,y = move
                if 0 <= x < x_limit and 0 <= y < y_limit and data[x][y].is_joinable((self.x, self.y)):
                    if data[self.x][self.y].can_joinable_without_join((x,y)):
                        data[x][y].joinable = False
                        player = (Player(x,y,self.answer + pos[position]))
                        if player.is_answer():return player
                        all_player.add(player)

        def is_answer(self):
            if (self.x, self.y) == fnish:
                return True

    class Wall:
        def __init__(self, num, x, y):
            b_num = format(num, "b")
            self.x = x
            self.y = y
            self.wall1 = "0" * (4 - len(b_num)) + b_num
            self.wall2 = self.wall1[1:] + self.wall1[0]
            self.wall3 = self.wall2[1:] + self.wall2[0]
            self.wall4 = self.wall3[1:] + self.wall3[0]
            self.wall1_joins = self._which_coor_can_join(self.wall1)
            self.wall2_joins = self._which_coor_can_join(self.wall2)
            self.wall3_joins = self._which_coor_can_join(self.wall3)
            self.wall4_joins = self._which_coor_can_join(self.wall4)
            self.joinable = True

        def _which_coor_can_join(self, num):
            num1, num2, num3, num4 = num
            data = set()
            if num1 == "0": data.add((self.x - 1, self.y))  # Nort tan girmek için
            if num2 == "0": data.add((self.x, self.y - 1))  # Westten girmek için
            if num3 == "0": data.add((self.x + 1, self.y))  # Southtan girmek için
            if num4 == "0": data.add((self.x, self.y + 1))  # Eastten girmek için
            return data

        def do_not_joinable(self):
            self.joinable = False

        def is_joinable(self, other_coor):
            # DO buraya ayn ıyer ekoymayıda ekle
            if self.joinable:
                if current == 0 and other_coor in self.wall1_joins:
                    return True
                elif current == 1 and other_coor in self.wall2_joins:
                    return True
                elif current == 2 and other_coor in self.wall3_joins:
                    return True
                elif current == 3 and other_coor in self.wall4_joins:
                    return True

        def can_joinable_without_join(self, other_coor):
            if current == 0 and other_coor in self.wall1_joins:
                return True
            elif current == 1 and other_coor in self.wall2_joins:
                return True
            elif current == 2 and other_coor in self.wall3_joins:
                return True
            elif current == 3 and other_coor in self.wall4_joins:
                return True

    data = [[y for y in x] for x in ar]
    start,fnish = (0,0), (0,0)
    for x, part in enumerate(ar):
        for y, element in enumerate(part):
            if type(element) == int:
                data[x][y] = Wall(element, x, y)
            elif element == "B":
                data[x][y] = Wall(0, x, y)
                start = (x,y)
            elif element =="X":
                data[x][y] = Wall(0, x, y)
                fnish = (x,y)
    def change_wall():
        nonlocal current
        current += 1
        if current == 4:
            current = 0
        for x in fake_player:
            x.answer = x.answer + ","

    Player(start[0],start[1],"")
    fake_player = set()
    fake_player.add(all_player.pop())
    t = 0
    while True:
        check = len(fake_player)
        for x in fake_player:
            result = x.move()
            if result:return result.answer.split(",")
        fake_player = all_player | fake_player
        if check == len(fake_player):
            t += 1
            change_wall()
            if t == 4:return
        else:
            t = 0
        all_player = set()