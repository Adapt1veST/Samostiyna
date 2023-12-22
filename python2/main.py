#my_list= [1,2,3]
#interaptor = iter(my_list)

#print(interaptor)
#print(next, interaptor)

#for elam in interaptor:
#    print(elam)

#class Counter:
#    def __init__(self, max_number):
#        self.i = 0
#        self.max_number = max_number
#
#    def __iter__(self):
#        self.i = 0
#        return self
#
#    def __next__(self):
#        self.i +=1
#        if self.i > self.max_number:
#            raise StopIteration
#        return self.i

#count = Counter(5)
#for elem in count:
#    print(elem)                    


#class Counter:
#    def __init__(self, max_number):
#        self.i = 0
#        self.max_number = max_number
#
#    def __iter__(self):
#       self.i = 0
#        return self
#
#    def __next__(self):
#        self.i +=1
#        if self.i > self.max_number or self.i > 9:
#            print("Error")
#            raise StopIteration
#        return self.i

#count = Counter(10)
#for elem in count:
#    print(elem) 

#def raise_to_the_degrees(number, max_degree):
# i=0
# for _ in range(max_degree):
#        yield number**i
#        i+=1

#res = raise_to_the_degrees(122345, 500)
#print(res)
#for _ in res:
# print(_)

#class Helper:
# def init(self, work):
#        self.work = work
# def call(self, work):
#        return f"I will help you with your {self.work}. Afterwards I will help  you with {work}"
#helper = Helper("homework")
#print(helper("cleaning"))

#def checker(function):
# def checker(*args, **kwargs):
#        try:
#                result = function(*args, **kwargs)
#        except Exception as exc:
#                print(f"We have problems {exc}")
#        else:
#                print(f"No problems. Result – {result}")
# return checker
#def calculate(expression):
#    return eval(expression)
#calculate = checker(calculate)
#calculate("2+2")


#import logging

#logging.basicConfig(level=logging.DEBUG)
#logging.debug("Debug:")
#logging.info("Info:")
#logging.error("Error:")
#logging.warning("Warning:")
#logging.critical("Critical:")

#max = 10
#max = "max"
#max = True
#a = 0
#if (a > 10):
#    a =+ 1

#class Xz():
#    speed = 7
#class Pok(Xz):
#    streng = 10

#kat = Pok()
#print(kat)  

#import logging
#logging.basicConfig(level=logging.DEBUG,
# filename="logs.log",
# filemode="w")
#logging.debug("debug")
#logging.info("info")

a = input()
print(2 + 2, a)
if (a == 4) :
    print("Right")
else :
    print("Wrong")    
