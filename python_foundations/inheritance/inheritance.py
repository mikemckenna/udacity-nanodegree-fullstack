class Parent():
    """Parent Class: test the concept of inheritance"""

    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name: " + self.last_name)
        print("Eye Color: " + self.eye_color)


class Child(Parent):
    """Child Class: test the concept of inheritance"""

    def __init__(self, last_name, eye_color, toy_count):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.toy_count = toy_count

    def show_info(self):
        print("Last Name: " + self.last_name)
        print("Eye Color: " + self.eye_color)
        print("Toy Count: " + self.toy_count)

mr_brady = Parent("Brady", "blue")
mr_brady.show_info()

greg = Child("Brady", "blue", 4)
greg.show_info()
print(greg.toy_count)
