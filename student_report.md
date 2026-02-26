## Tobias DiRito & Trevor Olson

## Objective
Identify the cryptographic misuse and recover the secret.

## Explanation
- What is broken?
    - Since ECB mode encrypts information using the same AES algorithm, if your message has repeating blocks, it will encrypt the output identically. In this example, the secret unencrypted message has repeating parts to it, and a SECURE encryption should produce unique ciphertext no matter the message, but ECB produced the exact same encryption. 
- Why is it insecure?
    - It is insecure because since it repeats, the attacker can get an idea of the structure of the secret message. If they were able to decrypt one part of the message, they can decrypt the whole thing since it repeats. In this specific example, we were able to see that the unique 16 bytes of ciphertext was the actual message and the rest was just padding that repeated.

## Solution
- Attack strategy
    - To solve this problem, we split the ciphertext into 16 byte blocks per the project specifications and then used Python's Counter dictionary to count how many occurences of each 16 byte block there are. After discovering the one block that was unique, we converted it to hex and used oracle to decrypt into the secret message.
- Code overview
    - We set a block size of 16 bytes and split the ciphertext into 16 byte blocks in an array: blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)].
    - We then used the Counter dictionary to count the number of occurences of each block in the array and identified the block with an occurence of 1 (unique block) and assigned it to a variable: 
    unique_block = None
    for block in counts:
        if counts[block] == 1:
            unique_block = block
    - Finally, we printed this unique block of ciphertext as a hex value for the user to input to oracle.

## Mitigation
- How should this be fixed?
    - The fix to this is shown in crypto_utils.py by use of AES-CBC. This creates a unique Initialization Vector for each iteration producing an entirely unique encrypted text regrardless of repeating plaintext. It is a non-deterministic mode of operation that scrambles each block of text so an attacker cannot see the "penguin outline" of your secret text.

