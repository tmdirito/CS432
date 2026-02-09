## C1_ECB – ECB Mode Weakness

This challenge demonstrates why AES-ECB is insecure.

You are given `challenge.bin`.

Tasks:
1. Detect ECB mode via repeated blocks
2. Locate the encrypted secret
3. Recover the plaintext secret

Hints:
- AES block size is 16 bytes
- Identical plaintext blocks encrypt identically in ECB
- The secret may not be block-aligned

