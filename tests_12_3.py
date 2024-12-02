import unittest
from suite_12_3 import Runner, Tournament, skip_if_frozen


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


if __name__ == "__main__":
    unittest.main(verbosity=2)