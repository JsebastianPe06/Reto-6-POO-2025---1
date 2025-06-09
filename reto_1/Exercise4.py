from .exeptions_functions import EmptyListError, generator_lists_numbers

#This function compares the sums of consecutive two numbers
#This function returns the largest sum
def greatest_sum_consecutive(lis):
    try:
        EmptyListError.check_empty_list(lis)
        if(len(lis) == 1):
            return None
        s = lis[0]+lis[1]
        for i in range(1, len(lis)-1):
            if(s < lis[i]+lis[i+1]):
                s = lis[i]+lis[i+1]
        return s
    except EmptyListError as e:
        print(e)

def run():
    while True:
        try:
            array_size:int = int(input("Enter the number of elements in the list: ")) 
            break
        except ValueError:
            print("Invalidated value")

    list_numbers = generator_lists_numbers(array_size)
    print(f"list: {list_numbers}")
    print(f"The greatest sum is: {greatest_sum_consecutive(list_numbers)}")