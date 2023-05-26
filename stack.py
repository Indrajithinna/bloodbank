class Stack:
 def __init__(self):
self.items =[ ]
def isEmpty(self):
 return self.items==[ ]
def push(self,items):
self.items.append(items)
def pop(self):
 return self.items.pop()
def display(self,i):
 return self.items[len(self.items)-i]
s=Stack()
print('Stack operation')print(s.isEmpty())
s.push(5)
s.push('DS with python')
print("Item in stack are")
print(s.display(1))
print(s.display(2))
print("The deleted item is:",s.pop())
print("The current elements in stack")
print(s.display(1)