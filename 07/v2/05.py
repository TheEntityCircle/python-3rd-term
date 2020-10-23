class Cursor:
    # Конструктор, принимающий два параметра - координаты X и Y
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.clicks = list()

    # Передвинуть по оси X на n и по оси Y на m
    # n, m - произвольные целые числа
    def move(self, n, m):
        self.x += n
        self.y += m

    # Клик в текущем положении курсора
    def click(self):
        self.clicks.append((self.x, self.y))

    # Вернуть количество кликов в заданном прямоугольнике
    def get_click_count(self, min_x, max_x, min_y, max_y):
        count = 0
        for c in self.clicks:
            if c[0] > min_x and c[0] < max_x and c[1] > min_y and c[1] < max_y:
                count += 1
        return count

"""
c = Cursor(100, 100)
c.click()
c.move(10, -10)
c.click()
c.move(-10, 10)
c.click()
print(c.get_click_count(95, 105, 95, 105))
print(c.get_click_count(0, 10, 0, 10))
"""