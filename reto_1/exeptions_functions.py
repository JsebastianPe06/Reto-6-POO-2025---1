from random import randint

class OutRangeError(Exception):
    def __init__(self, message="Error. Value out of range"):
        super().__init__(message)
    
    @staticmethod
    def check_out_range(minimun:int, value:int, maximun:int):
        if(value < minimun or value > maximun):
            raise OutRangeError()

class EmptyListError(Exception):
    def __init__(self, message="Error. The list is empty"):
        super().__init__(message)
    
    @staticmethod
    def check_empty_list(lis):
        if(len(lis) == 0):
            raise EmptyListError()

class NegativeNumberError(Exception):
    def __init__(self, message="Error. Value is negative"):
        super().__init__(message)
    
    @staticmethod
    def is_negative(value:int):
        if(value < 0):
            raise NegativeNumberError()

#This function generates a list of n random numbers
def generator_lists_numbers(n):
    m = []
    try:
        NegativeNumberError.is_negative(n)
        for i in range(n):
            m.append(randint(-1000, 1000))
    except NegativeNumberError as e:
        print(e)
    return m