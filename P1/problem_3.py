import sys
import heapq


class Node(object):
        
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    
    def __cmp__(self, other):
        if other == None:
            return -1
        if not isinstance(other, HeapNode):
            return -1
        return self.freq > other.freq

    # defining comparators less_than
    def __lt__(self, other):
        return self.freq < other.freq


class TreeLinkedList:

    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}


    # Creating 
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
            
            newnode_char = node1.char + node2.char
            newnode_freq = node1.freq + node2.freq

            merged = Node(newnode_char, newnode_freq)
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
    

    # Method to asist in decoding
    def get_decoded_text(self):
        updated_rev_map = {}
        for key, value in self.reverse_mapping.items():
            if len(value) == 1:
                updated_rev_map[key] = value

        return updated_rev_map

        


def huffman_encoding(data):

    tree = TreeLinkedList()
    letter_freq = tree.make_frequency_dict(data)

    tree.make_heap(letter_freq)
    tree.merge_nodes()
    tree.make_codes()

    encoded_text = tree.get_encoded_text(data)

    return encoded_text, tree
    
    

def huffman_decoding(data,tree):
    '''
    Decodes text enconded with basis on
    reverse mapping table
    '''

    updated_rev_map = tree.get_decoded_text()

    current = ""
    decoded_text = ""
    
    for bit in data:
        current += bit
        if current in updated_rev_map:
            character = updated_rev_map[current]
            decoded_text += character
            current = ""
    
    return decoded_text




# Test 1
if __name__ == "__main__":

    a_great_sentence = "The bird is the word"
    
    print("Test 1")
    # Prints - The size of the data is: 69
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Prints - The content of the data is: The bird is the word
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    encoded_data, tree = huffman_encoding(a_great_sentence)

    # Prints - The size of the encoded data is: 36
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Prints - The content of the encoded data is: 1000111111100100001101110000101110110110100011111111001101010011100001
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    
    # Prints - The size of the decoded data is: 69
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Prints - The content of the encoded data is: The bird is the word
    print ("The content of the encoded data is: {}\n".format(decoded_data))



# Test 2
if __name__ == "__main__":

    a_great_sentence = "The third-rate mind is only happy when it is thinking with the majority. The second-rate mind is only happy when it is thinking with the minority. The first-rate mind is only happy when it is thinking."

    print("Test 2")
    # Prints - The size of the data is: 250
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Prints - The content of the data is: The third-rate mind is only happy when it is thinking with the majority. The second-rate mind is only happy when it is thinking with the minority. The first-rate mind is only happy when it is thinking.
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    encoded_data, tree = huffman_encoding(a_great_sentence)

    # Prints - The size of the encoded data is: 136
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    '''Prints - The content of the encoded data is: 0111111110010100110111101001010101000011000101011011011010
                                         10100110001100111101000001001011100011101111011110110010011
                                         101011010100101001100100010011110010111110010011010010010111
                                         001101111010011111100001001111011011000100110011011110001101
                                         111001010011000110110011010100111010101100110111001011001000
                                         111111110010100101110101011010001110111101000011000101011011
                                         011010101001100011001111010000010010111000111011110111101100
                                         100111010110101001010011001000100111100101111100100110100100
                                         101110011011110100111111000010011110110110001001100110111100
                                         011011110010100110001100111101110101011001101110010110010001
                                         111111100101000110101110010101101111101011000101011011011010
                                         101001100011001111010000010010111000111011110111101100100111
                                         010110101001010011001000100111100101111100100110100100101110
                                         01101111010011111100001001111011011011001'''
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    # Prints - The size of the decoded data is: 250
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    '''Prints - The content of the encoded data is: The third-rate mind is only happy when it is thinking with the majority. 
                                         The second-rate mind is only happy when it is thinking with the minority. 
                                         The first-rate mind is only happy when it is thinking.'''
    print ("The content of the encoded data is: {}\n".format(decoded_data))


# Test 3
if __name__ == "__main__":

    a_great_sentence = "abababababa"

    print("Test 3")
    # Prints - The size of the data is: 60
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Prints - The content of the data is: abababababa
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    encoded_data, tree = huffman_encoding(a_great_sentence)

    # Prints - The size of the encoded data is: 28
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Prints - The content of the encoded data is: 10101010101
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    # Prints - The size of the decoded data is: 60
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Prints - The content of the encoded data is: abababababa
    print ("The content of the encoded data is: {}\n".format(decoded_data))

