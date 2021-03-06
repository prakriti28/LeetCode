# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listNodeConverter(lst: list) -> ListNode:
    if len(lst) == 0:
        return None
    head = ListNode(0)
    ptr = head
    for i, num in enumerate(lst):
        ptr.val = num
        if(i < len(lst) - 1):
            ptr.next = ListNode(0)
            ptr = ptr.next
    return head


def printListNode(ln: ListNode):
    while(ln != None):
        print(ln.val, end=" -> ")
        ln = ln.next
    print("")


def compareListNode(ln1: ListNode, ln2: ListNode) -> bool:
    # TODO: make sure there is no loop in it
    while ln1 != None and ln2 != None:
        if ln1.val != ln2.val:
            return False
        else:
            ln1 = ln1.next
            ln2 = ln2.next
    if ln1 == None and ln2 == None:
        return True
    else:
        return False
