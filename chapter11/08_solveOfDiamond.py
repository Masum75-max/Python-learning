class A:
    def show(self):
        print("আমি Class A")

class B(A):
    def show(self):
        print("আমি Class B")

class C(A):
    def show(self):
        print("আমি Class C")

# Class D একই সাথে B এবং C কে ইনহেরিট করছে। 
# যেহেতু B আগে (বামে) লেখা হয়েছে, তাই B-এর পাওয়ার বেশি!
class D(B, C):
    pass

obj = D()
obj.show() # আউটপুট কী হবে?