# Stack class

class Stack():
    ''' Stack class implements a last in first out LIFO algorithm'''
    def __init__(self, startingStackAsList=None):
        if startingStackAsList == None:
            self.dataList = [ ]
        else:
            self.dataList = startingStack[:]  # make a copy 
        
    def push(self, item):       
        self.dataList.append(item)

    def pop(self):
        if len(self.dataList) == 0:
            raise IndexError
        element = self.dataList.pop()
        return element

    def peek(self):
        # retrieve the top item, without removing it
        item = self.dataList[-1]
        return item

    def getSize(self):
        nElements = len(self.dataList)
        return nElements

    def show(self):
        # show the stack in a vertical orientation
        print('Stack is:')
        for value in reversed(self.dataList):
            print('   ', value)