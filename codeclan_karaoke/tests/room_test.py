import unittest
from classes.room import *
from classes.guest import *
from classes.song import *

class RoomTest(unittest.TestCase):


    def setUp(self):
        self.room1 = Room("Andrews Karaoke", 2)
        self.room2 = Room("Johns Karaoke", 3)
        self.guest1 = Guest("Keith", 300, "all the single ladies")
        self.guest2 = Guest("Rob", 50, "Without me")
        self.guest3 = Guest("Jenny", 20, "Have you ever seen the rain")
        self.guest4 = Guest("Patrick", 5, "Do I wanna know")
        self.guest5 = Guest("Roberta", 100, "How you remind me")
        self.song1 = Song("Have you ever seen the rain")
        self.song2 = Song("Life with you")
        self.song3 = Song("Forever in Blue Jeans")
        self.song4 = Song("Do I wanna know")
        self.song5 = Song("Without me")



    def test_check_room_name(self):
        self.assertEqual("Andrews Karaoke", self.room1.room_name)

    def test_check_room_starts_empty(self):
        self.assertEqual(0, len(self.room1.guest_list))

    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.assertEqual(1, len(self.room1.guest_list))

    def test_remove_guest_from_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.remove_guest()
        self.assertEqual(0, len(self.room1.guest_list))

    def test_add_song_to_room(self):
        self.room1.add_song_to_room(self.song1)
        self.assertEqual("Have you ever seen the rain", self.song1.song_name)

    def test_room_capacity(self):
        self.assertEqual(3, self.room2.room_capacity)

    def test_room_capacity_is_available(self):
        self.room1.add_guest_to_room(self.guest1)
        self.room1.add_guest_to_room(self.guest2)
        self.room1.add_guest_to_room(self.guest3)
        self.assertEqual(True, self.room1.room_has_capacity())

    def test_customer_has_enough_to_enter(self):
        self.assertEqual(True, self.guest1.guest_has_enough())
        