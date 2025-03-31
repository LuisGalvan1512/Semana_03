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
        self.length = 0  
        
## ---------------------------------------- ##
    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the linked list.
        
        Args:
            data: The data to store in the new node
        
        Returns:
            bool: True if the insertion was successful
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

        self.length += 1  
        return True
## ---------------------------------------- ##

    def display(self):
        if self.head is None:
            return "Empty list"
        current = self.head
        result = ""
        while current is not None:
            result += str(current.get_data()) + " -> "
            current = current.get_next()
        return result + "None"

# Código de prueba
if __name__ == "__main__":
    test_list = LinkedList()
    test_list.insert_at_beginning(30)
    test_list.insert_at_beginning(20)
    test_list.insert_at_beginning(10)

    test_list.insert_at_beginning(1)

    print("Linked list:")
    print(test_list.display())
    print("Length:", test_list.length)
