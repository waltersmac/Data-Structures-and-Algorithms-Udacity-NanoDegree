class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)


    def to_list(self):
        out_list = []
        cur_head = self.head
        while cur_head:
            out_list.append(cur_head.value)
            cur_head = cur_head.next
        return out_list




def union(llist_1, llist_2):
    
    return sorted(set(llist_1 + llist_2))



def intersection(llist_1, llist_2):
    
    intersection_list = []

    for i in llist_1:
        if i in llist_2:
            intersection_list.append(i)

    return sorted(set(intersection_list))





# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

# Print [1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65]
print (union(linked_list_1.to_list(),linked_list_2.to_list()))
# Prints [4, 6, 21]
print (intersection(linked_list_1.to_list(),linked_list_2.to_list()))



# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = [3,2,4,35,6,65,6,4,3,23]
element_4 = [1,7,8,9,11,21,1]

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)

# Prints [1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65]
print (union(linked_list_3.to_list(),linked_list_4.to_list()))
# Prints [] - No items
print (intersection(linked_list_3.to_list(),linked_list_4.to_list()))


# Test case 3
# Using 2 empty elements
linked_list_4 = LinkedList()
linked_list_5 = LinkedList()

element_4 = []
element_5 = []

for i in element_4:
    linked_list_4.append(i)

for i in element_5:
    linked_list_5.append(i)

# Prints [1, 7, 8, 9, 11, 21]
print (union(linked_list_4.to_list(),linked_list_5.to_list()))
# Prints [] - No items
print (intersection(linked_list_4.to_list(),linked_list_5.to_list()))
