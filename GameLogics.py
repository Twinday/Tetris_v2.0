import MyRandom as rnd
import static

class Level(object):
    def __init__(self, score):
        self.matrix = list()
        self.lup = (21, 0)
        self.width = 15
        self.height = 22
        self.score = score


    def create_level(self):
        is_not_empty_blocks = 11
        self.matrix.clear()
        for i1 in range(self.height - is_not_empty_blocks):
            row1 = []
            for j1 in range(self.width):
                row1.append(0)
            self.matrix.append(row1)
        for i2 in range(is_not_empty_blocks):
            row2 = []
            for j2 in range(self.width):
                row2.append(rnd.random_block())
            self.matrix.append(row2)

    def move_border(self, side):
        map = {
            'up': (self.lup[0] - 1, self.lup[1]),
            'down': (self.lup[0] + 1, self.lup[1]),
            'left': (self.lup[0], self.lup[1] - 1),
            'right': (self.lup[0], self.lup[1] + 1)
        }

        if side == 'up':
            if self.lup[0] > 0:
                self.lup = map[side]
        if side == 'down':
            if self.lup[0] < len(self.matrix) - 1:
                self.lup = map[side]
        if side == 'left':
            if self.lup[1] > 0:
                self.lup = map[side]
        if side == 'right':
            if self.lup[1] < len(self.matrix[0]) - 1:
                self.lup = map[side]

    def _shift(self, lst, steps):
        if steps < 0:
            steps = abs(steps)
            for i in range(steps):
                lst.append(lst.pop(0))
        else:
            for i in range(steps):
                lst.insert(0, lst.pop())


    def add_row(self):
        col_matrix = []
        for j in range(len(self.matrix[0])):
            col = []
            for i in range(len(self.matrix)):
                col.append(self.matrix[i][j])
            if col[0] == 0:
                self._shift(col, -1)
                col[-1] = rnd.random_block()
                col_matrix.append(col)

        for b in range(len(self.matrix[0])):
            for a in range(len(self.matrix)):
                self.matrix[a][b] = col_matrix[b][a]


    def _delete_4_more_same_blocks(self, boolmatrix):
        indexes = []
        count = 0
        for i in range(len(boolmatrix)):
            for j in range(len(boolmatrix[i])):
                if boolmatrix[i][j] == True:
                    indexes.append((i, j))
                    count += 1
        if count > 3:
            self.score += count*100
            for a in indexes:
                self.matrix[a[0]][a[1]] = 0


    def _check_empty_block_in_middle(self, column):
        indexes = []
        for row in range(len(self.matrix)):
            if self.matrix[row][column] == 0:
                indexes.append(row)

        if len(indexes) > 0:
            return (True, indexes)
        else:
            return (False, indexes)


    def _shift_empty_blocks(self, column, indexes):
        for i in indexes:
            a = []
            for row in range(i + 1):
                a.append(self.matrix[row][column])
            self._shift(a, 1)
            for k in range(i + 1):
                self.matrix[k][column] = a[k]

    def _check_empty_block_in_middle_in_all_columns(self):
        for col in range(len(self.matrix[0])):
            flag = self._check_empty_block_in_middle(col)
            if flag[0]:
                self._shift_empty_blocks(col, flag[1])


    def update(self):
        boolmatrix = static.create_false_boolmatrix(self.height, self.width)
        boolmatrix = static.try_search_neighbor(self.matrix, boolmatrix, self.lup[0], self.lup[1])
        self._delete_4_more_same_blocks(boolmatrix)
        self._check_empty_block_in_middle_in_all_columns()


    def check_game_over(self):
        for i in range(len(self.matrix[0])):
            if self.matrix[0][i] != 0:
                return True
        return False


    def __getitem__(self, key):
        return self.matrix[key[0]][key[1]]


    def get_lup(self):
        return self.lup


    def get_score(self):
        return self.score
