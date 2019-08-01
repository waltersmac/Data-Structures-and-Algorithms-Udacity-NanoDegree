import sys


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None



class Tree_nodes (object):
    def __init__(self, path):
        self.path = path
        self.nodes = []
        self.tree = []
        self.new_node = []
        self.new_nodes = []
        self.pos = 0

    

    def merge_nodes(self):
        while len(self.tree) > 1:
            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2




def to_set(data):

    data = list(data)
    char_freq = {}

    for letter in data:
        if letter in char_freq:
            char_freq[letter] += 1
        else:
            char_freq[letter] = 1
    
    char_freq = [[v, k] for k, v in char_freq.items()]

    return sorted(char_freq, reverse=True)



huffman_tree = []

def combine(nodes):

    pos = 0
    new_node = []

    if len(nodes) > 1:
        nodes.sort()

        nodes[pos].append("0")
        nodes[pos+1].append("1")

        combined_node1 = (nodes[pos][0] + nodes[pos+1][0])
        combined_node2 = (nodes[pos][1] + nodes[pos+1][1])

        new_node.append(combined_node1)
        new_node.append(combined_node2)

        newnodes = []

        newnodes.append(new_node)
        newnodes = newnodes + nodes[2:]
        nodes = newnodes

        huffman_tree.append(nodes)

        combine(nodes)

    return huffman_tree


def huffman_encoding(data):

    nodes = to_set(data)

    huffman_tree.append(nodes)

    return combine(nodes)



    


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