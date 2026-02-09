import sys
from collections import Counter
def solve(ciphertext):
    block_size = 16
    blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]

    from collections import Counter
    counts = Counter(blocks)

    unique_block = None
    for block in counts:
        if counts[block] == 1:
            unique_block = block

    print(f"Encrypted secret: {unique_block}")
    print(f"Hex Value: {unique_block.hex()}")
    print("Enter hex value of secret text into oracle to decrypt!")

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'rb') as f:
        ciphertext = f.read()
    solve(ciphertext)