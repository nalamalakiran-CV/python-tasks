"""Operator overloading:when an operator performs different actions
    it is said to exhibit polymorphism """

class maths:
    def __init__(self, marks):
        self.marks=marks

    def __add__(self, other):
        return self.marks+other.marks

class science:
    def __init__(self, marks):
        self.marks = marks

s1=maths(78)
s2=science(64)

print("marks = ", s1+s2)