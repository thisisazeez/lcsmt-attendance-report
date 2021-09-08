# class mystack:
#     def __init__(self):
#         self.data =[]

#     def length(self): #length of the list
#         return len(self.data)

#     def is_full(self): #check if the list is full or not
#         if len(self.data) == 5:
#             return True
#         else:
#             return False

#     def push(self, element):# insert a new element
#         if len(self.data) < 5:
#             self.data.append(element)
#         else:
#             return "overflow"

#     def pop(self): # # remove the last element from a list
#         if len(self.data) == 0:
#             return "underflow"
#         else:
#             return self.data.pop()
        
# a = mystack() # I create my object
# a.push(10) # insert the element
# a.push(23)
# a.push(25)
# a.push(27)
# a.push(11)
# print(a.length())
# print(a.is_full())
# print(a.data)
# print(a.push(31))
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop()) 


class myqueue:
    
    def __init__(self):
        self.data = []
    
    def length(self):
        return len(self.data)
    
    def enque(self, element):
        if len(self.data) < 5:
            return self.data.append(element)
        else:
            "overflow"
            
    def deque(self):
        if len(self.data) == 5:
            return "underflow"
        else:
            self.data.pop(0)
            
            
b = myqueue()
b.enque(2) # put the element into the queue
b.enque(3)
b.enque(4)
b.enque(5)
print(b.data)
b.deque()# # remove the first element that we have put in the queue
print(b.data)