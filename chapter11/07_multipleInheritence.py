class Father:
    def height(self):
        print("height is like fathers")

class Mother:
    def eyes(self):
        print("eyes are as beautiful as mothers")

# দুটি প্যারেন্ট ক্লাস কমা (,) দিয়ে লিখতে হয়
class Child(Father, Mother):
    pass

c = Child()
c.height() # Father থেকে এসেছে
c.eyes()   # Mother থেকে এসেছে