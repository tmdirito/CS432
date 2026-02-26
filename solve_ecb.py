import sys
from collections import Counter
def solve(ciphertext):
    block_size = 16
    blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)] # Split the ciphertext into 16-byte blocks

    counts = Counter(blocks) # count occurrences of each block

    unique_block = None
    for block in counts:
        if counts[block] == 1:
            unique_block = block # find unique block

    print(f"Encrypted secret: {unique_block}") # return the unique block
    print(f"Hex Value: {unique_block.hex()}") # return unique block as ciphertext
    print("Enter hex value of secret text into oracle to decrypt!")

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'rb') as f:
        ciphertext = f.read()
    solve(ciphertext)