#Errors created
class TypeListError(Exception):
    def __init__(self, message="Error, There is at least one data item in the"
    " list that is not of the expected type"):
        super().__init__(message)
    
    @staticmethod
    def check_list_type(lis, expect_type:type):
        if not all(isinstance(i, expect_type) for i in  lis):
            raise TypeListError()

class AmountDataError(Exception):
    def __init__(self, message="Error, The amount of data in the list is incorrect"):
        super().__init__(message)
    
    @staticmethod
    def check_amount_data_list(lis, num:int):
        if(len(lis) != num):
            raise AmountDataError()

class EquallyDataError(Exception):
    def __init__(self, message="Error, Operation is not allowed here if there is equal data in the list"):
        super().__init__(message)
    
    @staticmethod
    def check_equally_data_list(lis):
        seen = set()
        for item in lis:
            if item in seen:
                raise EquallyDataError()
            seen.add(item)