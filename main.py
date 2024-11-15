class Node():
    # Empty constructor
    def __init__(self, value = None, next = None, previous = None):
        # Define the node's basic properties "value", "next", "previous" and default them
        # Return this node
        self.value = value
        self.next = next
        self.previous = previous
        return
    
    def set(self, value):
        # Set this node's value to the given value
        # Return this node
        self.value = value
        return self
    
    def get_value(self):
        # Return the value of this node
        return self.value
    
    def get_next(self):
        # Return this node's next node
        return self.next
    
    def get_previous(self):
        # Return this node's previous node
        return self.previous
    
    def set_next(self, next):
        # Set this node's next node
        # Return this node
        self.next = next
        return self
    
    def set_previous(self, previous):
        # Set this node's previous node
        # Return this node
        self.previous = previous
        return self
    
class LinkedList():
    # Empty constructor 
    def __init__(self, head = None, tail = None):
        # Define the list's basic properties "size", "head" and "tail"
        # Default them to 0 and None respectively
        self.head = head
        self.tail = tail
        return
    
    '''
    REQUIRED METHODS TO PASS LAB
    '''
    def size(self):
        # Return the size of the list
        count = 0
        traverse = self.head
        while traverse:
            count += 1
            traverse = traverse.next
        return count
    
    def add(self, value):
        # Add the given value to the END of the list
        # If the list is empty make the value first
        # Return this list
        new = Node(value)
        if self.head == None:
            self.head = new
            self.tail = self.head
        else:
            traverse = self.head
            while traverse.next:
                traverse = traverse.next
            traverse.next = new
            new.previous = traverse
            self.tail = new      
        return
    
    def remove(self, index):
        # Remove the given index
        # Be sure to maintain the integrity of the list
        # If index is out of range or list is empty raise an IndexError with message "Index is out of range"
        # Return this list
        if index < 0:
            raise IndexError("Index is out of range")
        
        if self.head == None:
            raise IndexError("Index is out of range")

        current = self.head
        count = 0

        while current:
            if count == index:
                if current.previous == None:
                    current.next.previous = current.previous
                    self.head = current.next
                elif current.next == None:
                    current.previous.next = current.next
                    self.tail = current.previous
                else:
                    current.next.previous = current.previous
                    current.previous.next = current.next
                return
            count += 1
            current = current.next

        raise IndexError("Index is out of range")
    
    def get(self, index):
        # Return the value at the given index
        # If index is out of range raise an IndexError with message "Index is out of range"
        if index < 0:
            raise IndexError("Index is out of range")
        
        if self.head == None:
            raise IndexError("Index is out of range")
        
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.value
            count += 1
            current = current.next
        
        raise IndexError("Index is out of range")
        
    def get_node(self, index):
        # Return the node from the given index
        # If index is out of range raise an IndexError with message "Index is out of range"
        # Bonus points if optimized to be better than O(N) in worst case
        if index < 0:
            raise IndexError("Index is out of range")
        
        if self.head == None:
            raise IndexError("Index is out of range")
        
        current = self.head
        count = 0

        while current:
            if count == index:
                return current
            count += 1
            current = current.next
        
        raise IndexError("Index is out of range")
    
    def empty(self):
        # Return true or false if the list is empty
        if self.head == None:
            return False
        else:
            return True
    
    def first(self):
        # Return the first value in the list
        # If list is empty return None
        if self.head == None:
            return self.head
        return self.head.value
    
    def last(self):
        # Return the last value in the list
        # If list is empty return None
        if self.tail == None:
            return self.tail
        return self.tail.value
    
    def reverse(self):
        # Reverse the elements in this list
        # Be sure to maintain the integrity of the list
        # Return this list 
        if self.head == None:
            return
        current = self.tail
        while current:
            if current.next == None:
                newHead = current
                current.next = current.previous
                print(current.value)
            elif current.previous == None:
                newTail = current
                current.previous = current.next
                print(current.value)
                break
            else:
                current.next = current.previous
                current.previous = current.next
                print(current.value)
            current = current.previous
        self.head = newHead
        self.head.previous = None
        self.tail = newTail
        self.tail.next = None 
        return
        # This function works -- but only once. Don't know why.