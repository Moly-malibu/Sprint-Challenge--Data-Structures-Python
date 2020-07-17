class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev): # 3 -> 2 -> 1 -> None reverse None <- 3 <- 2 <- 1 
        if not self.head or not self.head.next_node:
            return self.head
        current_node = self.head
        previous_node = None
        while current_node: # loop: list if its not None 
            next_node = current_node.next_node #variable -> next node -> current node.
            current_node.next_node = previous_node #current node -> next node -> previos node
            previous_node = current_node #Update ->previos -> current node
            current_node = next_node #Update Current and next node.
        self.head = previous_node #set Current previos node -> last node -> initial list.      


    # def reverse_list(self, node, prev):
    #     if self.head is None:
    #         return None
    #     elif node.next_node:
    #         new_node = node.get_next()
    #         self.reverse_list(new_node, node)
    #     else:
    #         self.head = node
    #     node.set_next(prev)