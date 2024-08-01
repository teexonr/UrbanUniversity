import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        self.participants = sorted(self.participants, key=lambda x: x.speed, reverse=True)
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(*[{k: v.name for k, v in dict_.items()} for dict_ in cls.all_results], sep='\n')

    def test_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[2] == self.runner3)

    def test_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[2] == self.runner3)

    def test_3(self):
        tournament = Tournament(90, self.runner1, self.runner1, self.runner3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[3] == self.runner3)

    def test_4(self):
        tournament = Tournament(90, self.runner2, self.runner2, self.runner3)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[3] == self.runner3)
