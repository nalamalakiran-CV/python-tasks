"""Inheritance:1.single inheritance
               2.multiple inheritance
               3.multilevel inheritance

    In inheritance we will have base_class(parent class, super_class) from
    where the child_class(sub_class) will be inheriting the properties from the
    base_class. The base_class cannot inherit the properties from it's
    sub_classes"""

#single level inheritance

class Parent():
    def feature1(self):
        print("This is parent class feature")

class Child(Parent):
    def feature2(self):
        print("This is child class feature")

parent_obj = Parent()
parent_obj.feature1()
#parent class could only able to accesss its own features

#child class could access both parent class features as well as its own features
child_obj = Child()
child_obj.feature1()
child_obj.feature2()


