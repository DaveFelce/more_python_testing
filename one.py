class testthing:

    stuff = 'flipyou'

    def __init__(self):
        self.thing = 'hahaha'
        self.thing2 = 'hahahahahahahah'

    # def __getattr__(self, item):
    #     return 'panties'

    def __get__(self, instance, owner):
        print("In __get__")
        print(self)
        print(instance)
        print(owner)
        return "Not here"

    def __getattribute__(self, item):
        print('lalalalalala')
        return object.__getattribute__(self, item)

class davetest:
    testthing = testthing()


t = testthing()
print(t.thing)
p = davetest()
print(p.testthing)

def blahstuff():
    pass

class Foo(object):
    def __init__(self, a):
        self.a = a

    def bar(self, b):
        print("in bar")
        print(self)
        return self.a + b

    blahstuff = blahstuff

foo = Foo(1)
print(Foo.bar(foo, 5))
print(foo.blahstuff)
print(blahstuff.__get__({}, Foo))

print(Foo.bar)
print(Foo.blahstuff)
foo.blahstuff()
b = foo.bar
print(b(2))


class Team:
    def __init__(self, members):
        self.__members = members
        self.value = 1

    def __len__(self):
        return len(self.__members)

    def __contains__(self, member):
        return member in self.__members

    def __iter__(self):
        for i in range(1, 11):
            yield i

    def __next__(self):
        self.value += 1
        return self.value

justice_league_fav = Team(["batman", "wonder woman", "flash"])

# Sized protocol
print(len(justice_league_fav))

# Container protocol
print("batman" in justice_league_fav)
print("superman" in justice_league_fav)
print("cyborg" not in justice_league_fav)

assert hasattr(justice_league_fav, '__iter__')

myiter = iter(justice_league_fav)
print(myiter)
for i in range(1,3):
    print(next(myiter))

for i in justice_league_fav:
    print(i)

print(next(justice_league_fav))
print(next(justice_league_fav))

class TestManager:

    def __enter__(self):
        '''Context management protocol.  Returns self.'''
        print("in __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''Context management protocol.  Calls close()'''
        print("in __exit__")

with TestManager() as tm:
    print('doing test manager')
    raise Exception("Something went wrong")

print('hahahaha')

class CallBk:
    def __init__(self, val):
        self.val = val

    def __call__(self, *args, **kwargs):
        print(self.val * 2)

cb = CallBk(val=5)
cb()

a_var = [1,2]

def outer():
    a_var = [3,4]

    def inner():
        a_var.append(5)
        print(a_var)

    inner()

outer()

count = 1
def make_counter():
    def counter():
        global count
        print(count)
        count += 1
        return count
    return counter

d = make_counter()
d()
d()
d()
print(d)

p = 'things'
print(f'Things should be here:{p} but not here: not {p}')

