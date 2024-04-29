#Programming Task 1.
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
        self.previous = None
    
class DoublyLinkedList:
    def __init__(self): 
        self.head = None 
        
    def append(self, data):
        if self.head is None:
            newNode = Node(data)
            newNode.previous = None
            self.head = newNode
        else: 
            newNode = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.previous = current
            newNode.next = None
        
    def prepend(self, data):
        if self.head is None:
            newNode = Node(data)
            newNode.previous = None
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
            newNode.previous = None

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete(self, key):
        current = self.head 
        while current:
            if current.data == key and current == self.head:
                if not current.next:
                    current = None
                    self.head = None
                    return
                else:
                    nxt = current.next
                    current.next = None
                    nxt.previous = None
                    current = None
                    self.head = nxt
                    return
                     
            elif current.data == key:
                if current.next:
                    nxt = current.next
                    previous = current.previous
                    previous.next = nxt
                    nxt.previous = previous
                    current.next = None
                    current.previous = None
                    current = None
                    return 
                else:
                    previous = current.previous
                    previous.next = None
                    current.previous = None
                    current = None
                    return 
            current = current.next

first_User_Input = input("Create a doubly linked list (Type yes or no)?: ")
if first_User_Input == "yes" or first_User_Input == "Yes":
    dll = DoublyLinkedList()
    print("A Doubly Linked List have been created.")
    while "dll" in locals():    
        second_User_Input = input("Do you want to add, remove, print or end the doubly linked list (Type either add, remove, print or end): ")
        if second_User_Input == "add" or second_User_Input == "Add":
            element = input("Type the number or character do want to add: ")
            where = input("Where at the linked list do want to add it (Type either start or end): ")
            if where == "end" or where == "End":
                dll.append(element)
                print(element + " has been added to the end of the doubly linked list.")
            elif where == "start" or where == "Start":
                dll.prepend(element)
                print(element + " has been added to the start of the doubly linked list.")
            else:
                print("Command not recognized.")   
        elif second_User_Input == "remove" or second_User_Input == "Remove":
            element = input("Type the number or character do want to remove: ")
            dll.delete(element)
            print(element + " have been removed from the linked list.")
        elif second_User_Input == "print" or second_User_Input == "Print":
            dll.print()
        elif second_User_Input == "end" or second_User_Input == "End.":
            print("Program has ended.")
            break
        else: 
            print("Command not recognized.")

elif first_User_Input == "no" or first_User_Input =="No":
    print("A Doubly Linked List have not been created.")
    print("Program has ended.")
else: 
    print("Command not recognized.")

