class calculation():
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def __add__(self):
        return self.number1+self.number2
    def __sub__(self):
        return self.number1-self.number2
    def __mul__(self):
        return self.number1*self.number2
    def __divmod__(self):
        return self.number1/self.number2
    def decision(self,user_decision):
        if user_decision=='+':
            return self.__add__()
        if user_decision=='-':
            return self.__sub__()
        if user_decision=='*':
            return self.__mul__()
        if user_decision=='/':
            return self.__divmod__()
user_input = input("please type in your calculation: ")
'''user_input = user_input.strip().split(" ")'''
number_1 = int(user_input[0])

number_2 = int(user_input[2])
decision  = user_input[1]
"""print(number_1)
print(number_2)
print(user_decision)"""


calc=calculation(number_1,number_2)
Result=calc.decision(decision)
print(Result)
"""Result=calc.__sub__()
print(Result)
Result=calc.__mul__()
print(Result)
Result=calc.__divmod__()
print(Result)"""
