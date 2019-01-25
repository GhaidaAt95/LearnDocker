import random

class MyClass(object):
    var = 10
    greeting = 'Hello, my class'
    def callMe(self):
        print('Calling "Callme" method with instance: ')
        print('\tSelf is : ',self)
    
    def dothis(self):
        self.rand_val = random.randint(1,10)

class MyClass2(object):
    def set_val(self, val):
        self.value = val
    
    def get_val(self):
        return self.value

class MyInteger(object):
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            print("******Only Integers******")
            return
        self.val = val
    
    def get_val(self):
        return self.val

    def increment_val(self):
        self.val = self.val + 1

def test1():       
    this_obj = MyClass()
    that_obj = MyClass()

    print(this_obj)
    print('Var = ',this_obj.var)
    print('Greeting = ',this_obj.greeting)
    this_obj.callMe()
    this_obj.dothis()
    print("Instance Random Value {}".format(this_obj.rand_val))
    print('*'*70)

def test2():
    a = MyClass2()
    b = MyClass2()

    a.set_val(10)
    b.set_val(100)
    print('A value = [{}] and B value = [{}]'.format(a.get_val(), b.get_val()))

    a.value = "Hello"
    print('A value = [{}] and B value = [{}]'.format(a.get_val(), b.get_val()))

def test3():
    i = MyInteger()
    i.set_val(9)
    print("I = ",i.get_val())
    i.set_val("Hi")
    print("I = ",i.get_val())
    i.increment_val()
    print("I = ",i.get_val())
    
# test2()
test3()