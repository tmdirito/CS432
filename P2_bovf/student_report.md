# Buffer Overflow Exploitation Report

**Student Group: 8 -- Tobias DiRito & Trevor Olson**  
**04/27/2026:**  

---

## 1. Objective

Briefly describe the goal of this assignment.

- What is the program supposed to do?
    The program is supposed to demonstrate how a program can be exploited using a buffer overflow. It normally allocates 16 characters, asks for user input, and prints it back. However, the exploit write past the buffer and overwrites the return address of the secret function, forcing it to return to the attacker.
- What is the objective of the exploit?
    The objective of the exploit is to recover the plaintext secret in flag.txt by taking over the control flow using a buffer overflow exploit. By overflowing the buffer and using the address of openFlag(), we set the RIP to execute openFlag(), giving us the secret.
---

## 2. Program Analysis

### 2.1 Overview of the Code

- Describe the purpose of the program.
    The purpose of the program is to demonstrate buffer overflow exploits and how a program can be 
    forced into a "weird state" and become vulnerable to attack. 
- What does the `openFlag()` function do?
    The openFlag() function opens flag.txt in read more, reads it character by character and then prints the output to the screen.
- What does `main()` do?
    main() allocates a 16 byte character array on the stack, clears the memory and then uses scanf to read user input into the buffer before printing it out to the user. 

---

### 2.2 Identified Vulnerability

- Where is the vulnerability located?
    The vulnerability is located in main() at the scanf("%s", buffer) function call.
- Why is it unsafe?
    It is unsafe, because it does not restrict the user from overflowing the allocated buffer size of 16 bytes. It essentially reads the user input until it is finished, as oppsoed to checking the size of the input first

```c
    Vulnerable line: scanf("%s", buffer);

As seen in our screenshots, we used gdb to find the address of the openFlag() function and put that into our python code in order to open the flag. We then set the buffer size to 16 (as shown in ex1.c), and the saved RBP size to 8 (as discussed in lecture and pdfs of slides) so the exploit will run as desired when runnning the python script in conjunction with our C code.