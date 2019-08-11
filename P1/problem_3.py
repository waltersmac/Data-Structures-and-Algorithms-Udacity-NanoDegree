import sys
import heapq


class Node(object):
        
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __cmp__(self, other):
        if(other == None):
            return -1
        if(not isinstance(other, HeapNode)):
            return -1
        return self.freq > other.freq

    # defining comparators less_than and equals
    def __lt__(self, other):
        return self.freq < other.freq


class TreeLinkedList:

    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}


    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency


    def make_heap(self, frequency):
        for key, value in frequency.items():
            node = Node(key, value)
            heapq.heappush(self.heap, node)


    def merge_nodes(self):
        while(len(self.heap)>1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            

            merged = Node(node1.char + node2.char, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)


    def make_codes_helper(self, root, current_code):
        if root is None:
            return

        else:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            
            self.make_codes_helper(root.left, current_code + "0")
            self.make_codes_helper(root.right, current_code + "1")


    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    
    def get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text
    
        


def huffman_encoding(data):

    tree = TreeLinkedList()
    letter_freq = tree.make_frequency_dict(data)

    tree.make_heap(letter_freq)
    tree.merge_nodes()
    tree.make_codes()

    encoded_text = tree.get_encoded_text(data)

    return encoded_text, tree
    
    

def huffman_decoding(data,tree):
    pass





if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    #decoded_data = huffman_decoding(encoded_data, tree)

    #print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #print ("The content of the encoded data is: {}\n".format(decoded_data))