class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)

## ---------------------------------------- ##
    def list_length(self):
        """
        Count the number of nodes in the linked list.
        Returns:
            int: The number of nodes in the list.
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count
## ---------------------------------------- ##
# Código de prueba
if __name__ == "__main__":
    test_list = LinkedList()
    test_list.insert_at_end(10)
    test_list.insert_at_end(20)
    test_list.insert_at_end(30)

    print("List length:", test_list.list_length())
