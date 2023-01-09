import unittest


def is_unique(inp):
    return len(inp) == len(set(inp))


def get_marker(inp):
    packet_length = 4
    for i in range(len(inp)):
        input_slice = inp[i:i+packet_length]
        if is_unique(input_slice):
            return i + packet_length


def get_message_marker(inp):
    message_length = 14
    for i in range(len(inp)):
        input_slice = inp[i:i+message_length]
        if is_unique(input_slice):
            return i + message_length

class Day6Tests(unittest.TestCase):
    def test_four_char_uniqness(self):
        inp = 'abcd'
        self.assertTrue(is_unique(inp))
        inp = 'aacd'
        self.assertFalse(is_unique(inp))
        inp = 'abca'
        self.assertFalse(is_unique(inp))

    def test_get_marker(self):
        inp = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
        self.assertEqual(get_marker(inp), 7)
        inp = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
        self.assertEqual(get_marker(inp), 5)
        inp = 'nppdvjthqldpwncqszvftbrmjlhg'
        self.assertEqual(get_marker(inp), 6)
        inp = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
        self.assertEqual(get_marker(inp), 10)
        inp = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
        self.assertEqual(get_marker(inp), 11)

    def test_get_message_marker(self):
        inp = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
        self.assertEqual(get_message_marker(inp), 19)
        inp = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
        self.assertEqual(get_message_marker(inp), 23)
        inp = 'nppdvjthqldpwncqszvftbrmjlhg'
        self.assertEqual(get_message_marker(inp), 23)
        inp = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
        self.assertEqual(get_message_marker(inp), 29)
        inp = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
        self.assertEqual(get_message_marker(inp), 26)


def main():
    with open('input.txt', 'r', encoding='utf-8') as f:
        data = f.read().strip()
    print(get_marker(data))
    print(get_message_marker(data))
    unittest.main()
    return 0


if __name__ == "__main__":
    main()
