first = 'Мама мыла раму'
second = 'Рамена мало было'
compare = list(map(lambda x, y: x == y, first, second))

print(compare)
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for item in data_set:
                file.write(str(item) + '\n')

    return write_everything


from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = list(words)

    def call(self):
        return choice(self.words)
    def __call__(self):
        return self.call()

writer = get_advanced_writer('example.txt')
writer('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
