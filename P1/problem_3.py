import sys
import heapq
import os


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None



class Tree (object):
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}



def to_set(data):

    data = list(data)
    char_freq = {}

    for letter in data:
        if letter in char_freq:
            char_freq[letter] += 1
        else:
            char_freq[letter] = 1
    
    char_freq = [(k, v) for k, v in char_freq.items()]

    return char_freq




def huffman_encoding(data):

    char_tuple = to_set(data)
    
    


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