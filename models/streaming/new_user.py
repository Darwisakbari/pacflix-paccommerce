import random
import string
from data.streaming.data import data_user

class NewUser:
    def __init__(self, username):
        self.username = username

    def register(self, plan, referral_code=None):
        if self.username in data_user:
            print(f"Username {self.username} sudah terdaftar!")
            return None

        if referral_code:
            print(f"Kode referral '{referral_code}' terdeteksi! Kamu dapat diskon Rp10.000 di bulan pertama.")

        my_referral_code = f"{self.username.lower()}-{self._generate_code()}"
        data_user[self.username] = [plan, 1, my_referral_code]

        print(f"\nSelamat, {self.username}! Kamu berhasil daftar dengan {plan}.")
        print(f"Kode referral kamu: {my_referral_code} (bagikan ke teman!)")

        return my_referral_code

    def _generate_code(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))