class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, data):
        #Inserts the element to the last index of the stack.
        self.data.append(data)
    
    def pop(self):
        #Removes the last element in the stack.
        return self.data.pop()

    def prepop(self):
        #Removes the first element in the stack. 
        return self.data.pop(0)

    def display(self):
        #Displays all the elements within the stack.
        return self.data

stack = Stack()
for x in range(1, 21):
    #Inserts the numbers 1 to 20 into the stack.
    stack.push(x)
    x = x + 1

print(stack.display())


