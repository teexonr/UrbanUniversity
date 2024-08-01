import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('')
        [runner.walk() for _ in range(10)]
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('')
        [runner.run() for _ in range(10)]
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1, runner2 = [Runner('') for _ in range(2)]
        [(runner1.walk(), runner2.run()) for _ in range(10)]
        self.assertNotEqual(runner1.distance, runner2.distance)
