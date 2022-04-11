class Room:
    def __init__(self, input_room_name, input_capacity):
        self.room_name = input_room_name
        self.room_capacity = input_capacity
        self.guest_list = []
        self.song_list = []

    def add_guest_to_room(self, guest):
        self.guest_list = []
        self.guest_list.append(guest)
    
    def remove_guest(self):
        for guest in self.guest_list:
            self.guest_list.remove(guest)

    def add_song_to_room(self, new_song):
        self.song_list.append(new_song)

    def room_has_capacity(self):
        if self.room_capacity >= len(self.guest_list):
            return True
        else:
            return False




