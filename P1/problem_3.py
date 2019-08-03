import sys

huffman_tree = []


def combine(nodes):

    pos = 0
    new_node = []

    if len(nodes) > 1:
        nodes.sort()
        print(nodes)

        nodes[pos].append("0")
        nodes[pos+1].append("1")
        print(nodes)

        combined_node1 = (nodes[pos][0] + nodes[pos+1][0])
        combined_node2 = (nodes[pos][1] + nodes[pos+1][1])
        print(combined_node1)
        print(combined_node2)

        new_node.append(combined_node1)
        new_node.append(combined_node2)
        
        newnodes = []

        newnodes.append(new_node)
        newnodes = newnodes + nodes[2:]
        nodes = newnodes
        
        huffman_tree.append(nodes)
        
        #combine(nodes)

    return huffman_tree




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




def huffman_encoding(data):

    nodes = to_set(data)

    return sorted(combine(nodes), reverse=True)



    


def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    huffman_encoding(a_great_sentence)
    
    #encoded_data, tree = huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #print ("The content of the encoded data is: {}\n".format(encoded_data))

    #decoded_data = huffman_decoding(encoded_data, tree)

    #print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #print ("The content of the encoded data is: {}\n".format(decoded_data))