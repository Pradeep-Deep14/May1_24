class MyClass:
    x=1 #class variable

p1=MyClass()
p2=MyClass()

p1.x=2 #instance variable
print(p2.x)

#1
#when p2.x is called it calls the 
#class variable and assigns the value 1

