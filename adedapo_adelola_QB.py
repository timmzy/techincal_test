import unittest


def compare(first_string, second_string):
    """
    :param first_string: First string value
    :param second_string: First string value
    :return: Returns a string of > < = or Error
    """
    # Check if is a string
    if isinstance(first_string, str) and isinstance(second_string, str):
        # Make string same case if character, compare and return sign
        if first_string.upper() > second_string.upper():
            return ">"
        elif first_string.upper() < second_string.upper():
            return "<"
        else:
            return "="
    else:
        raise ValueError


"""
Test Case
"""
class TestCompare(unittest.TestCase):

    def test_gt_num(self):
        self.assertEqual(compare("1.2", "1.1"), ">", "It should return: '>'")

    def test_lt_num(self):
        self.assertEqual(compare("1.1", "1.5"), "<", "It should return: '<'")

    def test_gt_chr(self):
        self.assertEqual(compare("B", "A"), ">", "It should return: '>'")

    def test_lt_chr(self):
        self.assertEqual(compare("C", "F"), "<", "It should return: '<'")

    def test_complex_format(self):
        with self.assertRaises(ValueError):
            return compare("c", 1.5)


if __name__ == '__main__':
    unittest.main()
