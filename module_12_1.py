import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test = runner.Runner('Alice')
        for _ in range(10):
            test.walk()

        self.assertEqual(test.distance, 50)

    def test_run(self):
        test = runner.Runner('Alice')
        for _ in range(10):
            test.run()

        self.assertEqual(test.distance, 100)

    def test_challenge(self):
        test_1 = runner.Runner('Maria')
        test_2 = runner.Runner('Alice')
        for _ in range(10):
            test_1.run()
            test_2.walk()
        self.assertNotEqual(test_1.distance, test_2.distance)

if __name__ == '__main__':
    unittest.main()