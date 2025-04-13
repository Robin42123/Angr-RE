# Angr-RE

# Simple CrackMe - License Key Cracking with Angr

This repository contains a simple C program that checks a license key and an *Angr* Python script to crack it using symbolic execution.

## Files

-`SimpleCrackme.c`: A simple C program that checks the validity of a license key.
-`angr_crack.py`: A Python script that uses the Angr library to perform symbolic execution and find the correct license key.

# How to Use

1. Compile the C Program
To compile the C program, use the following command:
`gcc -o SimpleCrackme SimpleCrackme.c`

 2. Run the Angr Script
Make sure you have Angr installed in your Python environment:
`pip install angr`

Run the Angr script to crack the license key:
`python angr_crack.py`

The script will use **Angr** to perform symbolic execution and print out the correct license key.

### 3. Test the License Key
You can test the cracked license key by running the compiled `SimpleCrackme` program and entering the key:
`./SimpleCrackme`

#License
This project is for educational purposes only. Feel free to explore and experiment!