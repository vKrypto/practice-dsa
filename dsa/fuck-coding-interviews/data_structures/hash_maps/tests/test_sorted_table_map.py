# coding: utf-8
import random
import sys
import unittest

from ..sorted_table_map import SortedTableMap


class TestCase(unittest.TestCase):
    def setUp(self):
        self.empty_map = SortedTableMap()

        self.d1 = {'key': 'The phrase on the cover', 'value': "DON'T PANIC"}
        self.d2 = {'key': 'The answer to the ultimate question', 'value': 42}
        self.d3 = {'key': "God's final message", 'value': 'WE APOLOGIZE FOR THE INCONVENIENCE'}
        data = [self.d1, self.d2]

        self.map = SortedTableMap()
        self.dict = {}
        for d in data:
            self.map[d['key']] = d['value']
            self.dict[d['key']] = d['value']

        self.numbers = [-7, 2, 6, 1, 0, 9, 4]
        self.sorted_numbers = sorted(self.numbers)
        self.int_map = SortedTableMap()
        for i in self.numbers:
            self.int_map[i] = i

    def test__len__(self):
        self.assertEqual(len(self.empty_map), 0)
        self.assertEqual(len(self.map), len(self.dict))

    def test__iter__(self):
        self.assertEqual(list(self.empty_map), [])
        self.assertCountEqual(list(self.map), list(self.dict))

    def test__setitem__(self):
        self.map[self.d2['key']] = -42
        self.dict[self.d2['key']] = -42
        self.map[self.d3['key']] = self.d3['value']
        self.dict[self.d3['key']] = self.d3['value']
        self.assertEqual(len(self.map), len(self.dict))
        self.assertCountEqual([(k, v) for k, v in self.map.items()], [(k, v) for k, v in self.dict.items()])

    def test__getitem__(self):
        with self.assertRaises(KeyError):
            self.map['NOT EXIST']

        self.assertEqual(self.map[self.d1['key']], self.dict[self.d1['key']])
        self.assertEqual(self.map[self.d2['key']], self.dict[self.d2['key']])

    def test__delitem__(self):
        with self.assertRaises(KeyError):
            del self.map['NOT EXIST']

        del self.map[self.d1['key']]
        del self.dict[self.d1['key']]
        self.assertEqual(len(self.map), len(self.dict))
        self.assertCountEqual([(k, v) for k, v in self.map.items()], [(k, v) for k, v in self.dict.items()])

    def test_find_min(self):
        self.assertEqual(self.empty_map.find_min(), None)

        key, value = self.int_map.find_min()
        self.assertEqual(key, min(self.numbers))

    def test_find_max(self):
        self.assertEqual(self.empty_map.find_max(), None)

        key, value = self.int_map.find_max()
        self.assertEqual(key, max(self.numbers))

    def test_find_lt(self):
        key = random.choice(self.numbers)
        with self.subTest(key=key):
            keys = [k for k, v in self.int_map.find_lt(key)]
            index = self.sorted_numbers.index(key)
            expected = self.sorted_numbers[0:index]
            self.assertEqual(keys, expected)

        key = 3
        with self.subTest(key=key):
            keys = [k for k, v in self.int_map.find_lt(key)]
            expected = [-7, 0, 1, 2]
            self.assertEqual(keys, expected)

        key = -sys.maxsize
        with self.subTest(key=key):
            self.assertEqual(list(self.int_map.find_lt(key)), [])

    def test_find_le(self):
        key = random.choice(self.numbers)
        with self.subTest(key=key):
            keys = [k for k, v in self.int_map.find_le(key)]
            index = self.sorted_numbers.index(key)
            expected = self.sorted_numbers[0:index + 1]
            self.assertEqual(keys, expected)

        key = 3
        with self.subTest(key=key):
            keys = [k for k, v in self.int_map.find_le(key)]
            expected = [-7, 0, 1, 2]
            self.assertEqual(keys, expected)

        key = -sys.maxsize
        with self.subTest(key=key):
            self.assertEqual(list(self.int_map.find_le(key)), [])

    def test_find_gt(self):
        key = random.choice(self.numbers)
        with self.subTest(key=key):
            keys = [k for k, v in self.int_map.find_gt(key)]
            index = self.sorted_numbers.index(key)
            expected = self.sorted_numbers[index + 1:]
            self.assertEqual(keys, expected)

        key = 3
        with self.subTest(key=key):
            keys = [k for k, v in self.int_map.find_gt(key)]
            expected = [4, 6, 9]
            self.assertEqual(keys, expected)

        key = sys.maxsize
        with self.subTest(key=key):
            self.assertEqual(list(self.int_map.find_gt(key)), [])

    def test_find_ge(self):
        key = random.choice(self.numbers)
        with self.subTest(key=key):
            keys = [k for k, v in self.int_map.find_ge(key)]
            index = self.sorted_numbers.index(key)
            expected = self.sorted_numbers[index:]
            self.assertEqual(keys, expected)

        key = 3
        with self.subTest(key=key):
            keys = [k for k, v in self.int_map.find_ge(key)]
            expected = [4, 6, 9]
            self.assertEqual(keys, expected)

        key = sys.maxsize
        with self.subTest(key=key):
            self.assertEqual(list(self.int_map.find_ge(key)), [])

    def test_integration(self):
        for i in range(1, random.randint(2, 1000)):
            self.map[f'{i}'] = i
            self.dict[f'{i}'] = i
            if i % 5 == 0:
                del self.map[f'{i}']
                del self.dict[f'{i}']

        self.assertEqual(len(self.map), len(self.dict))
        self.assertCountEqual(list(self.map.items()), list(self.dict.items()))

    def test_find_range(self):
        # [-7, 0, 1, 2, 4, 6, 9]
        start_key, stop_key = 0, -1
        with self.subTest(start_key=start_key, stop_key=stop_key):
            keys = [k for k, v in self.int_map.find_range(start_key, stop_key)]
            expected = []
            self.assertEqual(keys, expected)

        start_key, stop_key = 0, 5
        with self.subTest(start_key=start_key, stop_key=stop_key):
            keys = [k for k, v in self.int_map.find_range(start_key, stop_key)]
            expected = [0, 1, 2, 4]
            self.assertEqual(keys, expected)

        start_key, stop_key = 7, 8
        with self.subTest(start_key=start_key, stop_key=stop_key):
            keys = [k for k, v in self.int_map.find_range(start_key, stop_key)]
            expected = []
            self.assertEqual(keys, expected)

        start_key, stop_key = 3, 10
        with self.subTest(start_key=start_key, stop_key=stop_key):
            keys = [k for k, v in self.int_map.find_range(start_key, stop_key)]
            expected = [4, 6, 9]
            self.assertEqual(keys, expected)

        start_key, stop_key = -6, -1
        with self.subTest(start_key=start_key, stop_key=stop_key):
            keys = [k for k, v in self.int_map.find_range(start_key, stop_key)]
            expected = []
            self.assertEqual(keys, expected)


if __name__ == '__main__':
    unittest.main()
