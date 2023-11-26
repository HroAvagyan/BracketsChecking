def solution(string):
    my_dict = {'(':')','{':'}','[':']'}
    lst = []
    for char in string:
        if char in my_dict.keys():
            lst.append(char)
        else:
            if not lst or my_dict[lst[-1]] != char:
                return False
            lst.pop()
    if lst:
        return False
    return True


string = '[[())]]'
print(solution(string))