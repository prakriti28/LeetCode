from LinkedList.ListNodeModule import listNodeConverter, compareListNode
from LinkedList.SwapNodesInPairs.Naive024 import Solution as naive
from LinkedList.SwapNodesInPairs.Recursive024 import Solution as recursive

def test_naive():
    assert compareListNode(naive().swapPairs(listNodeConverter([])), listNodeConverter([])) == True
    assert compareListNode(naive().swapPairs(listNodeConverter([1,2,3,4])), listNodeConverter([2,1,4,3])) == True
    assert compareListNode(naive().swapPairs(listNodeConverter([1,2,3,4,5])), listNodeConverter([2,1,4,3,5])) == True
    assert compareListNode(naive().swapPairs(listNodeConverter([1,2,3,4,5,6])), listNodeConverter([2,1,4,3,6,5])) == True

def test_recursive():
    assert compareListNode(recursive().swapPairs(listNodeConverter([])), listNodeConverter([])) == True
    assert compareListNode(recursive().swapPairs(listNodeConverter([1,2,3,4])), listNodeConverter([2,1,4,3])) == True
    assert compareListNode(recursive().swapPairs(listNodeConverter([1,2,3,4,5])), listNodeConverter([2,1,4,3,5])) == True
    assert compareListNode(recursive().swapPairs(listNodeConverter([1,2,3,4,5,6])), listNodeConverter([2,1,4,3,6,5])) == True