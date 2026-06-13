# test_blockpower.py
"""
Tests for BlockPower module.
"""

import unittest
from blockpower import BlockPower

class TestBlockPower(unittest.TestCase):
    """Test cases for BlockPower class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockPower()
        self.assertIsInstance(instance, BlockPower)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockPower()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
