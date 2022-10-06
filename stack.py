'''

Task 1

'''
def Stack():
    stack = []
    return stack

def size(stack):
    return len(stack)

def Emptystack(stack):
    if size(stack)==0:
        return true

def pushitem(stack, item):
    stack.append(item)

def pop(stack):
    if Emptystack(stack):
        return
    return stack.pop()

def reverse(string):
    n = len(string)
    stack = Stack()
    for i in range(0, n, 1):
        pushitem(stack,string[i])
    string = ""
    for i in range(0, n, 1):
        string += pop(stack)
    return string

string = "Something"
string = reverse(string)
print("Reversed: " + string)