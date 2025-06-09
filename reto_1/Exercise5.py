from copy import deepcopy

from .exeptions_functions import EmptyListError

#This function checks if two strings have the same characters
def same_characters(string1:str, string2:str):
    try:
        if(len(string1) != len(string2)):
            return False
        cop1 = list(string1)
        cop2 = list(string2)
        for char in cop1:
            if char in cop2:
                cop2.remove(char)
            else:
                return False
        return True
    except TypeError:
        print("There is an incompatible operation between data")
        return None

#This function forms groups of strings with the same characters into a list
def groups_same_characters(lis):
    try:
        EmptyListError.check_empty_list(lis)
        s = lis.copy()
        new_list = []
        while(len(s) != 0):
            group = [s[0]]
            for i in range(1, len(s)):
                if(same_characters(s[0], s[i])):
                    group.append(s[i])
            new_list.append(group)
            for i in group:
                s.remove(i)
        return new_list
    except EmptyListError as e:
        print(e)
        return []

#This function removes sublists from a list that contain only one element
def keep_groups(lis):
    try:
        EmptyListError.check_empty_list(lis) 
        t = len(lis)
        i = 0
        while(i < t):
            if(len(lis[i]) == 1):
                lis.remove(lis[i])
                t -= 1
            else:
                i += 1
        return lis
    except EmptyListError as e:
        print(e)
        return []

def check_instance_str(lis)->list[str]:
    copy = deepcopy(lis)
    for i in copy:
        if  not isinstance(i, str):
            copy.remove(i)
    return copy

def run():
    list_ = [11, "roma", "amor", "perro", "uno", "onu", "nou", "sol", "los", True]
    list_strings = check_instance_str(list_)
    formed_groups = keep_groups(groups_same_characters(list_strings))
    for i in range(len(formed_groups)):
        print(formed_groups[i])