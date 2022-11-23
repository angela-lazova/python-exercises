"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""
def isValid(self, s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    dic = {
        ']':'[',
        '}':'{',
        ')':'('
    }

    my_list = []
    for character in s:

        if character == '[' or character == '{' or character =='(':
            my_list.append(character)
        else:
            if my_list == []:
                return False
            
            last_element = my_list[-1]
            if dic[character] == last_element:
                my_list.pop()
            else:
                return False

    if my_list == []:
        return True
    else:
        return False