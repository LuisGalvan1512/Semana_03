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

## ---------------------------------------- ##
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
test_list = LinkedList()
test_list.insert_at_end(10)
test_list.insert_at_end(20)
test_list.insert_at_end(30)

# MOSTRAR EN CONSOLA
print(test_list.display()) 
