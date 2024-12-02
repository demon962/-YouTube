import unittest
from unittest import TestSuite, TextTestRunner

def skip_if_frozen(method):
    """Декоратор для пропуска тестов, если is_frozen = True"""

    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print(f"Тесты в этом кейсе ({self.__class__.__name__}) заморожены")
        else:
            method(self, *args, **kwargs)

    return wrapper


class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


class Tournament:
    def __init__(self, runners):
        self.runners = runners

    def start(self):
        results = []
        for runner in self.runners:
            distance = 100
            time = distance / runner.speed
            results.append((runner.name, time))

        results.sort(key=lambda x: x[1])

        return results

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_create_runner(self):
        usain = Runner('Усэйн', 10)
        self.assertEqual(usain.name, 'Усэйн')
        self.assertEqual(usain.speed, 10)

    @skip_if_frozen
    def test_another_runner(self):
        andrey = Runner('Андрей', 9)
        self.assertEqual(andrey.name, 'Андрей')
        self.assertEqual(andrey.speed, 9)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_tournament_result(self):
        usain = Runner('Усэйн', 10)
        andrey = Runner('Андрей', 9)
        nick = Runner('Ник', 3)
        tournament = Tournament([usain, andrey, nick])
        results = tournament.start()
        expected_results = [('Усэйн', 10), ('Андрей', 11.11111111111111), ('Ник', 33.333333333333336)]
        self.assertEqual(results, expected_results)


my_suite = TestSuite()
my_suite.addTest(RunnerTest('test_create_runner'))
my_suite.addTest(RunnerTest('test_another_runner'))
my_suite.addTest(TournamentTest('test_tournament_result'))


runner = TextTestRunner(verbosity=2)
runner.run(my_suite)