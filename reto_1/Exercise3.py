from .exeptions_functions import EmptyListError, generator_lists_numbers

#This function checks if a number is prime
def is_prime(n):
    if(n <= 1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i == 0):
            return False
    return True

#This function returns a list of prime numbers from the given list
def returns_prime_numbers(lis):
    s = []
    try:
        EmptyListError.check_empty_list(lis)
        for i in range(len(lis)):
            if(is_prime(lis[i])):
                s.append(lis[i])
    except EmptyListError as e:
        print(e)
    return s

def run():
    while True:
        try:
            array_size:int = int(input("Enter the number of elements in the list: "))
            break
        except ValueError:
            print("Invalidated value")

    list_numbers = generator_lists_numbers(array_size)

    print(f"list: {list_numbers}")
    print(f"list of prime numbers: {returns_prime_numbers(list_numbers)}")