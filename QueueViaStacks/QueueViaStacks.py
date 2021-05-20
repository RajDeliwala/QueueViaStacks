'''
Cracking the coding interview
Chapter 3 - Stacks and Queues
Stacks and Queues: Queues via Stacks
----------------------------------------
Question: Implement a MyQueue class which implements a queue using two stacks
Example: 
input: 
output: 
Constraits or Questions you need to ask:
Need to treat the 2 stacks in the background as a queue
push items into the pushstack and when it comes time for you to pop, transfer items into the popstack causing the order of items to be useable as a .dequeue
of a queue
Solution notes:
Class should have 2 stacks, 1 for pop and 1 for push
.push() is simple, just append onto the pushStack
.pop() should have logic for the following situation
- Both stacks are empty, return error
- If popStack is empty transfer the items from pushStack into popStack
- if pushStack is empty, we already transfered the items so just pop fromt he popStack
- if both stacks have values, that means we already transfered the items needing to be popped so just pop from popStack
'''

class MyQueue:

    def __init__(self):
        self.popStack = []
        self.pushStack = []

    def push(self, item):
        #For push() we just need to add to the push stack
        self.pushStack.append(item)
        
    def pop(self):
        #Returnable value 
        poppedValue = 0
        if self.popStack == [] and self.pushStack == []:
            return print(IndexError("Queue is empty, please pop content onto the Queue "))

        #First we check the logic for 
        if self.popStack == []:
            while self.pushStack != []:
                self.popStack.append(self.pushStack.pop())
            poppedValue = self.popStack.pop()
            return poppedValue
        
        if self.pushStack == []:
            poppedValue = self.popStack.pop()
            return poppedValue

        poppedValue = self.popStack.pop()
        return poppedValue
  

queue = MyQueue()

queue.push(4)
queue.push(6)
queue.push(7)
queue.push(9)
queue.push(10)
queue.pop() #4
queue.pop() #6
queue.push(2)
queue.pop() #7
queue.push(9)




print(queue.popStack[::-1] + queue.pushStack)



            
    

