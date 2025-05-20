class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre  = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
# my_linked_list = LinkedList(2)
# my_linked_list.append(1)

# print(my_linked_list.pop_first())

# print(my_linked_list.pop_first())

# print(my_linked_list.pop_first())

# ---------------05-Prepend ------------------
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node 
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

# my_linked_list = LinkedList(2)
# my_linked_list.append(3)

# my_linked_list.prepend(1)

# my_linked_list.print_list()


# -----------------------06-Pop First-------------

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
# my_linked_list = LinkedList(2)
# my_linked_list.append(1)

# my_linked_list.print_list()

# # (2) Items - Returns 2 Node
# print(my_linked_list.pop_first())
# # (1) Item - Returns 1 Node
# print(my_linked_list.pop_first())
# # (0) Items - Returns None
# print(my_linked_list.pop_first())


# ---------------07-Get------------------

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
# my_linked_list = LinkedList(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)

# print(my_linked_list.get(2))

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# my_linked_list.set_value(1,4)

# my_linked_list.print_list()

#---------------09-Insert--------------

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
my_linked_list = LinkedList(0)
my_linked_list.append(2)

my_linked_list.insert(1,1)

my_linked_list.print_list()


#