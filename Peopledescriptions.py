# Aly Batch
# People Class
# 11/13/19


class Person:
    def __init__(self, name, hair, eyes, age):
        self.name = name
        self.hair = hair
        self.eyes = eyes
        self.age = age

    def description(self):
        print(f"My name is {self.name} and I am {self.age} years old. I have {self.hair}, my eyes are {self.eyes}.")

