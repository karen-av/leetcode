class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        print(list1)
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
x = ListNode([1,2,3])


print((x.val))


import itertools
x = '11112'
s = set()
for p in itertools.permutations(x):
    a = (''.join(p))
    s.add(''.join(p))
print(a, s)

d = ['f','s']
def te(x):
    return " ".join(x) 
print(te(d))

m, n = 3, 4
l = [[] for i in range(n)]
print(l)