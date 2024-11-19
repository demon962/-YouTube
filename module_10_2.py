import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days_passed = 0

    def run(self):
        global enemies_left

        print(f"{self.name}, на нас напали!")

        while enemies_left > 0:
            if enemies_left <= self.power:
                enemies_left -= self.power
                break

            enemies_left -= self.power
            self.days_passed += 1
            time.sleep(1)
            print(f"{self.name} сражается {self.days_passed}..., осталось {enemies_left} воинов.")

        if enemies_left <= 0:
            print(f"{self.name} одержал победу спустя {self.days_passed} день(ей)!")




enemies_left = 100

knight_1 = Knight("Артур", 20)
knight_2 = Knight("Ланселот", 25)
knight_3 = Knight("Гавейн", 15)

knight_1.start()
knight_2.start()
knight_3.start()

knight_1.join()
knight_2.join()
knight_3.join()

print("Битвы окончены! Рыцари победили всех врагов.") 