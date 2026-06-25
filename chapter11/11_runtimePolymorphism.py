class Cricket:
    def play(self):
        print("ব্যাট-বল দিয়ে ক্রিকেট খেলা হচ্ছে।")

class Football:
    def play(self):
        print("পা দিয়ে ফুটবল খেলা হচ্ছে।")

# এটি একটি সাধারণ ফাংশন যা রান-টাইমে সিদ্ধান্ত নেবে
# এখানে কোনো টাইপ ডিফাইন করা নেই (যেমন সি++ এ Parent* obj লিখতে হতো)
def start_game(game_obj):
    game_obj.play() # রান-টাইমে পাইথন দেখবে মেথডটা আছে কিনা

# অবজেক্ট তৈরি
cric = Cricket()
foot = Football()

# রান-টাইম পলিমরফিজম অ্যাকশন!
start_game(cric) # আউটপুট: ব্যাট-বল দিয়ে ক্রিকেট খেলা হচ্ছে।
start_game(foot) # আউটপুট: পা দিয়ে ফুটবল খেলা হচ্ছে।