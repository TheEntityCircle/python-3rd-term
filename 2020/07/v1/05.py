class GasStation:
    # Конструктор, принимающий один параметр - ёмкость резервуара колонки
    # Резервуар создаётся пустой
    def __init__(self, c):
        self.capacity = c
        self.volume = 0

    # Залить в резервуар колонки n литров топлива
    # Если столько не влезает в резервуар - не заливать ничего, выбросить exception
    def fill(self, n):
        if self.volume + n > self.capacity:
            raise Exception("Too large amout to fill")
        self.volume += n

    # Заправиться, забрав при этом из резервура n литров топлива
    # Если столько нет в резервуаре - не забирать из резервуара ничего, выбросить exception
    def tank(self, n):
        if self.volume - n < 0:
            raise Exception("Too large amout to tank")
        self.volume -= n

    # Запросить остаток топлива в резервуаре
    def get_limit(self):
        return self.volume
