import unittest
from classes.song import *

class SongTest(unittest.TestCase):
    pass

    def setUp(self):
        self.song_name = Song("Have you ever seen the rain")

    def test_check_guest_name(self):
        self.assertEqual("Have you ever seen the rain", self.song_name.song_name)

