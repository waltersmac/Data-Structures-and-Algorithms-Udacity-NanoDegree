import sys
from collections import deque


class Node(object):
        
    def __init__(self,char, freq):
        self.char = value
        self.freq = freq
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"



class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"




class TreeLinkedList:

    def __init__(self):
        self.root = None
        
    def set_root(self,value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def combine_nodes(self, node1, node2):
        pass


    # Helper function - Create set of tuples lowest to highest frequencies
    def to_set(self, data):

        data = list(data)
        char_freq = {}

        for letter in data:
            if letter in char_freq:
                char_freq[letter] += 1
            else:
                char_freq[letter] = 1
    
        char_freq = [(v, k) for k, v in char_freq.items()]

        return sorted(char_freq)
        




def huffman_encoding(data):

    tree = TreeLinkedList()
    letter_freq = tree.to_set(data)
    return letter_freq
    #return sorted(combine(nodes), reverse=True)





def huffman_decoding(data,tree):
    pass









if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    print(huffman_encoding(a_great_sentence))
    
    #encoded_data, tree = huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #print ("The content of the encoded data is: {}\n".format(encoded_data))

    #decoded_data = huffman_decoding(encoded_data, tree)

    #print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #print ("The content of the encoded data is: {}\n".format(decoded_data))