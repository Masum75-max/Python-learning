from abc import ABC, abstractmethod

# এটি আমাদের Abstract Class (একটি নিয়ম বা ফ্রেমওয়ার্ক)
class Vehicle(ABC): 
    
    @abstractmethod
    def start_engine(self):
        pass # এখানে কোনো কোড থাকবে না, শুধু নিয়ম বলে দেওয়া হলো

    @abstractmethod
    def stop_engine(self):
        pass

# চাইল্ড ক্লাসকে অবশ্যই উপরের দুটি নিয়ম মানতে হবে
class Car(Vehicle):
    def start_engine(self):
        print("কার ইঞ্জিন চালু হলো... ব্রুম ব্রুম!")
        
    def stop_engine(self):
        print("কার ইঞ্জিন বন্ধ হলো।")

# v = Vehicle() # এটি রান করলে এরর আসবে (Abstract class-এর অবজেক্ট হয় না)

my_car = Car()
my_car.start_engine() # আউটপুট: কার ইঞ্জিন চালু হলো...