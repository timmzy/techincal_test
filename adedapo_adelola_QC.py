from datetime import datetime
import time
import unittest


class GeoDistributionCache(object):
    """
    This Object performs Least Recently Used algorithm.
    It also has a time expiry feature
    """

    def __init__(self, capacity, time_length):
        """
        :param capacity: an integer that specifies the size of the cache
        :param time_length: an number value that specifies when an allocated item in a cache can expire
        """
        self.time_length = time_length
        self.capacity = capacity
        self.cache = {}
        self.arrival_time = {}

    def set_item(self, value):
        key, item = value
        key = str(key)
        # If the item already exists reorder the cache by placing the item first
        if key in self.cache.keys():
            del self.cache[key]

        # If the capacity is full remove the least recently used item
        if len(self.cache) > self.capacity:
            self._pop_last_item()

        # Re order the cache before inputting an item then reorder the cache
        self._reorder()
        self.cache[key] = item
        self.arrival_time[key] = datetime.now()
        self._reorder()

    def _reorder(self):
        # Create a place holder that takes in a new reorder cache then sets it into the cache
        place_holder = {}
        time_placeholder = {}
        positions = list(self.cache.keys())
        positions.reverse()
        for index in positions:
            place_holder[index] = self.cache[index]
            time_placeholder[index] = self.arrival_time[index]
        self.cache = place_holder
        self.arrival_time = time_placeholder

    def _pop_last_item(self):
        # Remove the last item
        positions = list(self.cache.keys())
        positions.reverse()
        del self.cache[positions[-1]]

    def evaluate_cache(self):
        # Check the list of expired items in the cache first before you remove them
        now = datetime.now()
        key_removal = []
        for key in self.arrival_time:
            if (now - self.arrival_time[key]).seconds >= self.time_length:
                key_removal.append(key)

        for key in key_removal:
            del self.cache[key]
            del self.arrival_time[key]

    def get_cache(self):
        # Return the list of cache item
        return list(self.cache.items())


"""
Test Case
"""
class TestLRU(unittest.TestCase):

    def test_cache_behaviour(self):
        cache = GeoDistributionCache(3, 20)
        cache.set_item((1, 10))
        cache.set_item((2, 50))
        cache.set_item((3, 90))
        cache.set_item((2, 60))
        get_cache = cache.get_cache()
        self.assertEqual(get_cache, [('2', 60), ('3', 90), ('1', 10)],
                         "The result should be ('2', 60), ('3', 90), ('1', 10)")

    def test_cache_behaviour_with_time(self):
        cache = GeoDistributionCache(3, 10)
        cache.set_item((1, 10))
        time.sleep(5)
        cache.set_item((2, 50))
        time.sleep(4)
        cache.set_item((3, 90))
        time.sleep(6)
        cache.set_item((2, 60))
        cache.evaluate_cache()
        get_cache = cache.get_cache()
        self.assertEqual(get_cache, [('2', 60), ('3', 90)],
                         "The result should be ('2', 60), ('3', 90)")


if __name__ == '__main__':
    unittest.main()
