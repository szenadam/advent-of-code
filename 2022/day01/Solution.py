
import unittest


class SolutionTest(unittest.TestCase):
    def test_oneElf(self):
        self.assertEqual(1, self.f([1]))
        self.assertEqual(3, self.f([1, 2]))
        self.assertEqual(6, self.f([1, 2, 3]))

    def test_TwoElves(self):
        self.assertEqual(2, self.f([1, 0, 2]))

    def f(self, inp):
        s = 0
        result = 0
        for i in inp:
            if i == 0:
                if s > result:
                    result = s
                s = 0
            s += i
        return result


if __name__ == '__main__':
    unittest.main()
