"""Method overloading: if a method can perform more than one task
                       then it is called method overloading
                       The method overloading is not possible in
                       python
                       we can achieve this by writing same method with
                       several parameters"""

class overload:
    def sum(self, a= None, b= None, c= None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!= None and b!= None:
            print(a+b)
        else:
            print('enter minimum two arguments')
x = overload()
x.sum(2,3,4)
x.sum(25)