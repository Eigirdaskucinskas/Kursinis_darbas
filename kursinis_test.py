import unittest
import os
from kursinis import RomanToDecimal, DecimalToRoman, HistoryManager

class TestRomanToDecimal(unittest.TestCase):
    def setUp(self):
        self.converter = RomanToDecimal()

    def test_valid_conversions(self):
        """Test standard Roman numeral inputs"""
        self.assertEqual(self.converter.convert("X"), 10)
        self.assertEqual(self.converter.convert("IX"), 9)
        self.assertEqual(self.converter.convert("MMMCCLXI"), 3261)
        self.assertEqual(self.converter.convert("iv"), 4)  # Test case sensitivity

    def test_invalid_romans(self):
        """Test that invalid strings raise ValueError"""
        invalid_inputs = ["IIII", "ABC", " ", "VV", "IC"]
        for val in invalid_inputs:
            with self.subTest(val=val): # subTests help identify which specific value failed
                with self.assertRaises(ValueError):
                    self.converter.convert(val)

class TestDecimalToRoman(unittest.TestCase):
    def setUp(self):
        self.converter = DecimalToRoman()

    def test_valid_conversions(self):
        """Test standard integer inputs"""
        self.assertEqual(self.converter.convert(1), "I")
        self.assertEqual(self.converter.convert(44), "XLIV")
        self.assertEqual(self.converter.convert(3999), "MMMCMXCIX")

    def test_out_of_range(self):
        """Test boundary limits (1-3999)"""
        with self.assertRaises(ValueError):
            self.converter.convert(0)
        with self.assertRaises(ValueError):
            self.converter.convert(4000)

class TestHistoryManager(unittest.TestCase):
    def test_singleton_behavior(self):
        """Ensure HistoryManager always returns the same instance"""
        h1 = HistoryManager()
        h2 = HistoryManager()
        self.assertIs(h1, h2)

    def test_file_creation(self):
        """Verify that history file handling doesn't crash"""
        history = HistoryManager()
        history.filename = "test_history.txt" # Use a dummy file
        history.save_result("X", 10, "Roman to Decimal")
        
        self.assertTrue(os.path.exists(history.filename))
        
        # Cleanup
        history.clear_history()
        self.assertFalse(os.path.exists(history.filename))

if __name__ == "__main__":
    unittest.main()