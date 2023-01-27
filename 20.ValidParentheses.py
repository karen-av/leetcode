"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Дана строка s, содержащая только символы '(', ')', '{', '}', '[' и ']', 
определите, является ли входная строка допустимой.

Входная строка является допустимой, если:

Открытые скобки должны быть закрыты скобками того же типа.
Открытые скобки должны быть закрыты в правильном порядке.
Каждая закрытая скобка имеет соответствующую открытую скобку того же типа.
 

Example 1:

Input: s = "()"
Output: true

"""

def isValid(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == '(':
            l = ')'
        elif s[i] == '[':
            l = ']'
        elif s[i] == '{':
            l = '}'
        else: return False
        if s[i+1] == l:
            s = s[:i] + s[i+2:]
            i = 0
            #print(s)
        else:
            i +=1
    if len(s) > 0:
        return False
    return True
    


s = "()"
k = "()[]{}"
l = "(]"
n = "{[]}"
j = "([)]"
w = "){"
u = "[([]])"
#assert(isValid(s)) == True, 's'
#assert(isValid(k)) == True, 'k'
#assert(isValid(l)) == False, 'l'
#assert(isValid(n)) == True, 'n'
#assert(isValid(j)) == False, j
#assert(isValid(w)) == False, 
assert(isValid(u)) == False, u