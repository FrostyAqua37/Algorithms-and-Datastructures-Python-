#Programming Task 1.
class Node:
    def __init__(self, data): 
        #Initialization of the nodes.
        self.data = data
        self.next = None
        self.previous = None
    
class DoublyLinkedList:
    def __init__(self): 
        self.head = None 
        
    def append(self, data):
        #Inserts values at the end of the list
        if self.head is None:
            #Creates a head node if there isnt one
            newNode = Node(data)
            newNode.previous = None
            self.head = newNode
        else: 
            #Creates a node and inserts the value if there is a head node.
            newNode = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.previous = current
            newNode.next = None
        
    def prepend(self, data):
        #Inserts values at the front of the list
        if self.head is None:
            #Creates a head one if there isnt one
            newNode = Node(data)
            newNode.previous = None
            self.head = newNode
        else:
            #Creates a node at the front of the list and inserts the value
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
            newNode.previous = None

    def print(self):
        #Displays the current node in the linked list. 
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete(self, key):
        #Removes nodes in the linked list based on number or character. 
        current = self.head 
        while current:
            if current.data == key and current == self.head:
                #Checks if the current node value is the same as the number/character we want to remove and if its the head node
                if not current.next:
                    #Removes the head node
                    current = None
                    self.head = None
                    return
                else:
                    #Removes the head node when there is more than 1 node in the list 
                    nxt = current.next
                    current.next = None
                    nxt.previous = None
                    current = None
                    self.head = nxt
                    return
                     
            elif current.data == key:
                #Checks if the node value is the same as the number/character we want to remove
                if current.next:
                    #Removes the a node when there is many nodes in a list
                    nxt = current.next
                    previous = current.previous
                    previous.next = nxt
                    nxt.previous = previous
                    current.next = None
                    current.previous = None
                    current = None
                    return 
                else:
                    #Removes the last node in the list
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

