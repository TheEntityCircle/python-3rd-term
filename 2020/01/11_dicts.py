"""
Для хранения составных данных есть приличное количество вариантов.
Возьмём для старта и для примера dict. Это примерно как map в C++, хотя, конечно, не совсем.
"""

# Пусть у нас есть два человека. У каждого есть имя и возраст.
user_a = {
    'name': "A",
    'age': 20
}
user_b = {
    'name': "UserB",
    'age': 17
}
user_c = {
    'name': "C",
    'age': 25
}

# Сделаем из них массив
users = [user_a, user_b, user_c]

# Обойдём людей, отсортировав их по возрасту
# (sorted не меняет исходный массив users)
for user in sorted(users, key = lambda u: u['age']):
    print("User %s, age %d" %(user['name'], user['age']))

print("===============")

# Отсортируем людей по имени, меняя исходный массив.
# Потом обойдём отсортированное.
users.sort(key = lambda u: u['name'])
for user in users:
    print("User %s, age %d" % (user['name'], user['age']))