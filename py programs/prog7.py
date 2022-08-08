"""polymorphism
Duck typing: In duck typing we don't need a type to call an existing method
on an object """

class car:
    def engine(self):
        print("red colour")
        print("petrol engine")

class bike:
    def engine(self):
        print("black colour")
        print("petrol engine")

def invoke_engine(obj):
    obj.engine()

fourwheeler= car()
invoke_engine(fourwheeler)

twowheeler = bike()
invoke_engine(twowheeler)

