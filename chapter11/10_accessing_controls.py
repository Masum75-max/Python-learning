class Parent:
    def __init__(self):
        self.public_val = "আমি পাবলিক"
        self._protected_val = "আমি প্রোটেক্টেড"
        self.__private_val = "আমি প্রাইভেট"

# চাইল্ড ক্লাস (যা Parent কে ইনহেরিট করছে)
class Child(Parent):
    def check_access(self):
        # ১. পাবলিক অ্যাক্সেস (খুব সহজে হবে)
        print(self.public_val) 
        
        # ২. প্রোটেক্টেড অ্যাক্সেস (C++ এর মতোই চাইল্ড ক্লাস এটা পাবে)
        print(self._protected_val) 
        
        # ৩. প্রাইভেট অ্যাক্সেস (এখানেই এরর আসবে!)
        # print(self.__private_val) # এটি আনকমেন্ট করলে AttributeError আসবে

# --- রান করে টেস্ট করি ---
obj = Child()
obj.check_access()