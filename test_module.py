import unittest
import combat_tracker

class Unitests(unittest.TestCase):
    
    def test_dam_equals_soak_dam(self):
        tracker = combat_tracker.Tracker(20, 4, 10)
        tracker.damage(6)
        actual = tracker.get_stats()
        expected = (18, 4, 4)
        self.assertEqual(actual, expected, "Expected current health, and soak to be less than what they were set to.")
    
    def test_soak_dam_equal_to_soak(self):
        tracker = combat_tracker.Tracker(20, 4, 5)
        tracker.damage(4, 5)
        actual = tracker.get_stats()
        expected = (19, 3, 5)
        self.assertEqual(actual, expected, "Expected current health, and armor to be less than what they were set to, and soak to be at max value.")
    
    def test_dam_greater_than_armor(self):
        tracker = combat_tracker.Tracker(20, 4, 10)
        tracker.damage(6, 8)
        actual = tracker.get_stats()
        expected = (18, 4, 2)
        self.assertEqual(actual, expected, "Expected current health, and soak to be less than what they were set to.")
    
    def test_dam_less_than_armor(self):
        tracker = combat_tracker.Tracker(20, 4, 10)
        tracker.damage(3, 4)
        actual = tracker.get_stats()
        expected = (20, 4, 6)
        self.assertEqual(actual, expected, "Expected current soak to be less than what it was set to, and health and armor to stay the same.")
    
    def test_get_max_stats(self):
        tracker = combat_tracker.Tracker(20, 4, 10)
        tracker.damage(3, 4)
        actual = tracker.get_max_stats()
        expected = (20, 4, 10)
        self.assertEqual(actual, expected, 'Expected to get max stats without any change.')
    
    def test_heal(self):
        tracker = combat_tracker.Tracker(20, 1, 5)
        tracker.damage(4)
        tracker.heal(2)
        actual = tracker.get_stats()
        expected = (19, 1, 1)
        self.assertEqual(actual, expected, "Expected health to be 1 less than what it was initialy set at.")
    
    def test_heal_greater_than_current_health(self):
        tracker = combat_tracker.Tracker(20, 1, 5)
        tracker.damage(4)
        tracker.heal(6)
        actual = tracker.get_stats()
        expected = (20, 1, 1)
        self.assertEqual(actual, expected, "Expected health to be at max value.")
    
    def test_reset_stats(self):
        tracker = combat_tracker.Tracker(20, 1, 5)
        tracker.damage(4)
        tracker.reset_stats()
        actual = tracker.get_stats()
        expected = (20, 1, 5)
        self.assertEqual(actual, expected, "Expected health to be at max value.")
    
    def test_set_current_stats(self):
        tracker = combat_tracker.Tracker(20, 4, 10)
        tracker.set_current_stats(15, 2, 5)
        actual = tracker.get_stats()
        expected = (15, 2, 5)
        self.assertEqual(actual, expected, "Expected value of the current_stats to be set to new values.")
    
    def test_set_initial_stats(self):
        tracker = combat_tracker.Tracker(20, 4, 10)
        actual = tracker.get_max_stats()
        expected = (20, 4, 10)
        self.assertEqual(actual, expected, "Expected results entered into the init function.")
    
    def test_set_max_stats(self):
        tracker = combat_tracker.Tracker(15, 1, 5)
        tracker.set_max_stats(20, 2, 10)
        actual = tracker.get_max_stats()
        expected = (20, 2, 10)
        self.assertEqual(actual, expected, 'Expected value of the max_stats to be set to new values.')
        
    def test_soak_dam_greater_than_current_soak(self):
        tracker = combat_tracker.Tracker(20, 4, 10)
        tracker.damage(15)
        actual = tracker.get_stats()
        expected = (8, 3, 5)
        self.assertEqual(actual, expected, "Expected current health, armor, and soak to be less than what it was set to.")
    
    def test_soak_reduced_to_negative_value(self):
        tracker = combat_tracker.Tracker(20, 2, 5)
        tracker.damage(10)
        actual = tracker.get_stats()
        expected = (10, 0, 5)
        self.assertEqual(actual, expected, "Expected current health, armor, and soak to be less than what it was set to.")
    
    def test_to_string(self):
        tracker = combat_tracker.Tracker(20, 2, 5)
        tracker.damage(4)
        actual = str(tracker)
        expected = 'stats: H[18/20] A[2/2] S[1/5]\n'
        self.assertEqual(actual, expected, 'Expected a different string representation.')
        
