import struct

#1.) Replace with actual address to open the flag
open_flag_addr = 0xdeadbeef  

#2.) Fill the buffer (size)
payload = b"A" * ??
#3.) overwrite saved RBP (size)
payload += b"B" * ?

payload += struct.pack("<Q", open_flag_addr)  # overwrite return address

print(payload)