#import sys

#print(sys.executable)
#print(sys.version)
#print(sys.platform)
#print(sys.argv)

#for _ in dir(__builtins__):
#    print(_)

#import inspect
#import requests

#print(inspect.ismodule(requests))
#print(inspect.isclass(requests))
#print(inspect.isfunction(requests))

#class Father:
#   def xz (self):
#   height = 100
#class Daughter(Father):
#    def xz1 (self):
#      weight = 150

#vikt = Daughter()   
#print(vikt)   

#class Father:
#    def xz (self):
#      height = 100
#class Daughter:
#    def xz1 (self):
#      weight = 150
#class Zahar(Father, Daughter):
#    pass

#kid = Zahar()
#print(kid)

#max = [1, 2, 3, 4]

#for i in max:
#    print(i)

#vik = 10

#if vik == 10:  
#    print("True")
#else:
#      print("False") 

#class Ok:
#    def __init__(self):
#        self = 100  
#xiz = Ok
#print(xiz)

#print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")

#try:
# print("start code")
# print("error")
# print("No errors")
#except:
# print("We have an error")
# print("code after capsule")

#try:
# print("start")
# print(progress)
# print("Finish")
#except:
# print("START")
# print("FINISH")

#try:
# print("start")
# print("progress")
# print("Finish")
#except:
# print("START")
# print("FINISH")

#try:
#    try:
#        print("start code")
#        print("error")
#        print("No erorrs")
#    except SyntaxError:
#        print("Wrong Syntax") 
#except NameError as error:
#    print(error) 

#try:
#    print("hello")
#    print(error)
#except:
#    print("You have problem") 
#else:
#    print("No problem")   
#finally:
#    print("You got it")   

#def checker(var_1):
# if type(var_1)!= str:
#  raise TypeError(f"Sorry, we can’t work with {type(var_1)}, "f"we need class str")
# else:
#  return var_1
#first_var = 10
#checker(first_var)

#class BuildingEror(Exception):
# def str(self):
#        return f"With so much material the  house cannot be built!"
#def check_material(amount_of_material, limit_value):
#        if amount_of_material > limit_value:
#              return "enough material"
#        else:
#                raise BuildingEror(amount_of_material)

#materials = 123
#check_material(materials, 300)


class Money(Exception):
    def str(self):
        return f"Therer aren't enough money"
def check_money(amount_of_money, limit):
    if amount_of_money > limit:
        return "enough money"
    else:
            raise Money(amount_of_money)   

money = 102
check_money(money, 101)                     
