#Multilevel inheritance
class Parent():
    def feature1(self):
        print("Parent feature")

class Child1(Parent):
    def feature2(self):
        print("child1 feature")

class Child2(Child1):
    def feature3(self):
        print("child2 feature")

child2_obj= Child2()
child2_obj.feature1()
child2_obj.feature2()
child2_obj.feature3()




