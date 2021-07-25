class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Hello my name is " + self.name)

    def check_over_18(self):
        if self.age > 18:
            return True
        else:
            return False
# add a method of check_over_18 that will return True or False
# based on the persons age
# create two differently aged person objects and test your code!!!


john = Person('john', 17)
print(john.check_over_18())
doe = Person('doe', 19)
print(doe.check_over_18())
