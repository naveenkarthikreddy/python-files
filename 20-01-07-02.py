# Python next() Function
# Python next() function is used to fetch next item
# from the collection. It takes two arguments an
# iterator and a default value and returns an element.
# This method calls on iterator and throws an error
# if no item is present. To avoid the error,
# we can set a default value.

# node is a mixture of data and next or both next and prev
class Node:
    def __init__(self, value=None, next=None):
        #  def __init__(self, value=None, next=None,prev=None): it
        # in the case of doubly linked list
        # we are taking the none as the default
        # value if we did not pass any value to it
        # if we pass any value it will take that value
        self.value = value
        self.next = next


class LinkedList:
    # all the functionalities will be executed here only
    def __init__(self):
        self.head = None

    def insert(self):
        pass

    def delete(self):
        pass


# this are taken care by node class
n1 = Node(3)
n2 = Node(7)
n3 = Node(2)
n4 = Node(9)

# this is taken care by linked list class
# we used to define functionalities also ..
LL = LinkedList()
LL.head = n1

# this is taken care by the node class
n1.next = n2
n2.next = n3
n3.next = n4

# n2.prev = n1
# n3.prev = n2
# n4.prev = n3
# this are in the case of doubly linked list
