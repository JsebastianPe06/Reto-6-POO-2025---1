from .exeptions_functions import EmptyListError

#This function checks if a string is a palindrome
def is_palindrome(cad):
    try:
        EmptyListError.check_empty_list(cad)
        for i in range(len(cad)//2):
            if(cad[i] != cad[-i-1]):
                return False
        return True
    except EmptyListError as e:
        print(e)
        return False

def run():
    character:str = input("Enter a character string: ")

    print(f"Is it palindrome?: {is_palindrome(character)}")