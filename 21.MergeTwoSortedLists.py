"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Вам даны главы двух отсортированных связанных списков list1 и list2.

Объедините эти два списка в один отсортированный список. 
Список должен быть составлен путем сращивания узлов первых двух списков.

Верните главу объединенного связанного списка.
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def mergeTwoLists(list1, list2):

    # если какой-то из списков пустой, то возвращаем доугой список
    if list1.val == 0:
        return list2
    if list2.val == 0:
        return list1

    # Выбираем меньшее число из двух списков
    if list1.val <= list2.val:
        mergedHead = list1
        list1 = list1.next
    else:
        mergedHead = list2
        list2 = list2.next
    
    mergedTail = mergedHead

    while list1 != None and list2 != None:
        if list1.val <= list2.val:
            tmp = list1
            list1 = list1.next
        else:
            tmp = list2
            list2 = list2.next
        
        mergedTail.next = tmp
        mergedTail = tmp
    
    if list1 != None:
        mergedTail.next = list1
    elif list2 != None:
        mergedTail.next = list2

    
    return mergedHead
        



#list_1 = [1,2,4]
#list_2 = [1,3,4]
#print(mergeTwoLists(list_1, list_2))

#assert(mergeTwoLists([1,2,4], [1,3,4])) == [1,1,2,3,4,4]
#assert(mergeTwoLists([], [])) == []
#assert(mergeTwoLists([], [0])) == [0]


"""
def mergeTwoLists(list1, list2):
    for i in list1:
        list2.append(i)
    return sorted(list2)
"""