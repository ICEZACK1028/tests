print("Hola buenas tardes")

class Car():

    def __init__(self, motor, wheels):
        
        self.motor = motor
        self.wheels = wheels
    
    def motor(self, number):
        
        self.motor *= number
        print(f"wow your motor is {self.motor}")

