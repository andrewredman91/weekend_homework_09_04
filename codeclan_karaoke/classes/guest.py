class Guest:
    def __init__(self, input_guest, input_money, input_fav_song):
        self.guest_name = input_guest
        self.guest_purse = input_money
        self.guest_fav_song = input_fav_song

    def guest_has_enough(self):
        if self.guest_purse >= 20:
            return True
        else:
            return False

    # def guest_no_enough(self, customer_purse)

