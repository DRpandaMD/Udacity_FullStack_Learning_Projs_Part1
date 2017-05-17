class Parent():
    """docstring for Parent"""

    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color
        return

    def show_info(self):
        print("Last Name: " + self.last_name)
        print("Eye Color: " + self.eye_color)
        pass


class Child(Parent):
    """docstring for Child"""
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
        return


BillyBob = Parent("Billy", "Brown")
# print(BillyBob.last_name)
BillyBob.show_info()

Mikey = Child("Zarate", "Brown", 9000)
print(Mikey.number_of_toys)
Mikey.show_info()
