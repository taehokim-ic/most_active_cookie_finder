import unittest
import sys
import os 
sys.path.insert(0, '..')
# sys.path.append(os.path.dirname(os.getcwd()))

from scripts import most_active_cookie

class TestMostActiveCookie(unittest.TestCase):
    def test_correct_