import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(data):
    freq = defaultdict(int)
    for char in data:
        freq[char] += 1

    # Create a priority queue (min-heap)
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # Generate Huffman codes
    def generate_codes(node, code="", codes={}):
        if node:
            if node.char is not None:
                codes[node.char] = code
            generate_codes(node.left, code + "0", codes)
            generate_codes(node.right, code + "1", codes)
        return codes

    root = heap[0]
    huffman_codes = generate_codes(root)

    # Encode the data
    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, huffman_codes

# Example usage
data = "huffman encoding"
encoded_data, huffman_codes = huffman_encoding(data)
print("Encoded Data:", encoded_data)
print("Huffman Codes:", huffman_codes)
