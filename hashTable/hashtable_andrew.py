# hashtable_andrew.py

# Andrew Cunningham
# 20 Apr 2025

'''
Implements a chaining hashtable
'''

class hash_table_andrew:
    def __init__(self, size):
        self.hashTable = [None] * size
        self.size = size

    class __Node:
        '''private inner class to use as nodes for the hashtable buckets'''
        def __init__(self, key, value, next = None):
            self.key = key
            self.value = value
            self.next = next

    def __hash(self, key):
        '''uses python hash to create a unique hash'''
        return hash(key) % len(self.hashTable)
    
    def put(self, key, value):
        '''adds value to the hashtable using the key to hash with'''
        index = self.__hash(key)
        new_node = self.__Node(key, value, None)

        # The spot is empty
        if self.hashTable[index] == None:
            self.hashTable[index] = new_node
            return
        
        # the spot contains a node, let's find the end of that linked list
        curr_node = self.hashTable[index]
        while curr_node.next != None:
            curr_node = curr_node.next
        
        # found the end, append the node
        curr_node.next = new_node

        self.size += 1

        return
    
    def get(self, key):
        '''Returns the value associated with Key, None if key not found'''
        index = self.__hash(key)
        curr_node = self.hashTable[index]
    
        if curr_node == None:
            # The bucket was empty
            return None
        
        while (curr_node.key != key):
            # the payload wasn't key
            curr_node = curr_node.next
            if curr_node == None:
                # hit the end of the linked list
                return None
            
        # the curr_node currently is the target
        return curr_node.value
    
    def remove(self, key):
        '''removes, and returns, the value associated with key. None if not found'''
        index = self.__hash(key)

        if self.hashTable[index] == None:
            # There was no node at that spot
            return None
        
        curr_node = self.hashTable[index]

        if curr_node.key == key:
            # the <key, value> is the head
            self.hashTable[index] = curr_node.next
            self.size -= 1
            return curr_node.value
        
        while curr_node.next != None:
            if curr_node.next.key == key:
                # the <key, value> is next, save the value and skip over it in
                # the linked list
                value = curr_node.next.value
                curr_node.next = curr_node.next.next
                self.size -= 1
                return value
        
        # we have hit the end of the linked list in the bucket
        return None
    
    def print_hashtable(self):
        '''Prints the table'''
        for i, node in enumerate(self.hashTable):
            print(f"[{i}]:", end=" ")
            if node is None:
                print("None")
            else:
                chain = []
                while node is not None:
                    chain.append(f"({node.key}: {node.value})")
                    node = node.next
                print(" -> ".join(chain))