"""Multiple inheritance: Here a child_class will be sub-classing
                        two super_classes"""

class superclass():
    def feature1(self):
        print("super_class")

class subclass1():
    def feature2(self):
        print("subclass1")

class subclass2(superclass,subclass1):
    def feature3(selfself):
        print("sublcass2")

subclass2_obj = subclass2()
subclass2_obj.feature1()
subclass2_obj.feature2()
subclass2_obj.feature3()




