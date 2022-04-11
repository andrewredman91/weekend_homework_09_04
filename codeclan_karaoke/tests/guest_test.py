import unittest
from classes.guest import *

class GuestTest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Charles", 40, "Hit me baby one more time")

    def test_check_guest_name(self):
        self.assertEqual("Charles", self.guest1.guest_name)
    



