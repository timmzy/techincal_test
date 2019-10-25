import unittest

def check_overlap(first_cord, second_cord):
    """
    :param first_cord:
    :param second_cord:
    :return: Returns a string whether it overlaps or not
    """
    x1, x2 = first_cord
    x3, x4 = second_cord
    # Create Node for calculations
    test1 = x1 - x3
    test2 = x1 - x4
    test3 = x2 - x3
    test4 = x2 - x4
    # Counter to check if it overlaps or not
    positive_counter = 0
    negative_counter = 0
    total_test = [test1, test2, test3, test4]
    for test in total_test:
        if test > 0:
            positive_counter += 1
        else:
            negative_counter += 1

    if positive_counter == 4 or negative_counter == 4:
        return "Lines do not overlap"
    else:
        return "Lines overlap"


"""
Test Case
"""
class TestOverlap(unittest.TestCase):

    def test_not_overlap(self):
        self.assertEqual(check_overlap((1, 5), (2, 6)), "Lines overlap", "The result should be: 'Lines overlap'")

    def test_overlap(self):
        self.assertEqual(check_overlap((1, 5), (6, 8)), "Lines do not overlap", "The result should be: 'Lines do not overlap'")


if __name__ == '__main__':
    unittest.main()
