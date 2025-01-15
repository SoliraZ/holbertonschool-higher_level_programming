# 🐍 Python If/Else, Loops, Functions

This repository contains various Python scripts that demonstrate basic programming concepts related to if/else statements, loops, and functions.

## 📋 Tasks

### 0. ➕ Positive or Negative
This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.

- **File:** `0-positive_or_negative.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ ./0-positive_or_negative.py 
    -4 is negative
    user@ubuntu:~/$ ./0-positive_or_negative.py 
    0 is zero
    user@ubuntu:~/$ ./0-positive_or_negative.py 
    -3 is negative
    user@ubuntu:~/$ ./0-positive_or_negative.py 
    -10 is negative
    user@ubuntu:~/$ ./0-positive_or_negative.py 
    10 is positive
    user@ubuntu:~/$ ./0-positive_or_negative.py 
    -5 is negative
    user@ubuntu:~/$ ./0-positive_or_negative.py 
    6 is positive
    user@ubuntu:~/$ ./0-positive_or_negative.py 
    7 is positive
    user@ubuntu:~/$ ./0-positive_or_negative.py 
    5 is positive
    user@ubuntu:~/$ 
    ```

### 1. 🔢 The Last Digit
This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.

- **File:** `1-last_digit.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ ./1-last_digit.py
    Last digit of 4205 is 5 and is less than 6 and not 0
    user@ubuntu:~/$ ./1-last_digit.py
    Last digit of -626 is -6 and is less than 6 and not 0
    user@ubuntu:~/$ ./1-last_digit.py
    Last digit of 1144 is 4 and is less than 6 and not 0
    user@ubuntu:~/$ ./1-last_digit.py
    Last digit of -9200 is 0 and is 0
    user@ubuntu:~/$ ./1-last_digit.py
    Last digit of 5247 is 7 and is greater than 5
    user@ubuntu:~/$ ./1-last_digit.py
    Last digit of -9318 is -8 and is less than 6 and not 0
    user@ubuntu:~/$ ./1-last_digit.py
    Last digit of 3369 is 9 and is greater than 5
    user@ubuntu:~/$ ./1-last_digit.py
    Last digit of -5224 is -4 and is less than 6 and not 0
    user@ubuntu:~/$ ./1-last_digit.py
    Last digit of -4485 is -5 and is less than 6 and not 0
    user@ubuntu:~/$ ./1-last_digit.py
    Last digit of 3850 is 0 and is 0
    user@ubuntu:~/$ ./1-last_digit.py
    Last digit of 5169 is 9 and is greater than 5
    user@ubuntu:~/$ 
    ```

### 2. 🔤 Print Alphabet
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- **File:** `2-print_alphabet.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ ./2-print_alphabet.py
    abcdefghijklmnopqrstuvwxyzuser@ubuntu:~/$
    ```

### 3. 🔡 Print Alphabet (except q and e)
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- **File:** `3-print_alphabt.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ ./3-print_alphabt.py
    abcdfghijklmnoprstuvwxyzuser@ubuntu:~/$
    ```

### 4. 🔢 Hexadecimal Printing
Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal.

- **File:** `4-print_hexa.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ ./4-print_hexa.py
    0 = 0x0
    1 = 0x1
    2 = 0x2
    3 = 0x3
    4 = 0x4
    5 = 0x5
    6 = 0x6
    7 = 0x7
    8 = 0x8
    9 = 0x9
    10 = 0xa
    11 = 0xb
    12 = 0xc
    13 = 0xd
    14 = 0xe
    15 = 0xf
    16 = 0x10
    17 = 0x11
    18 = 0x12
    ...
    96 = 0x60
    97 = 0x61
    98 = 0x62
    user@ubuntu:~/$
    ```

### 5. 🔢 Print Numbers
Write a program that prints numbers from 0 to 99.

- **File:** `5-print_comb2.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ ./5-print_comb2.py
    00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
    user@ubuntu:~/$ 
    ```

### 6. 🔢 Print Combinations
Write a program that prints all possible different combinations of two digits.

- **File:** `6-print_comb3.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ ./6-print_comb3.py
    01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
    user@ubuntu:~/$ 
    ```

### 7. 🔡 islower
Write a function that checks for lowercase character.

- **File:** `7-islower.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 7-main.py
    #!/usr/bin/env python3
    islower = __import__('7-islower').islower

    print("a is {}".format("lower" if islower("a") else "upper"))
    print("H is {}".format("lower" if islower("H") else "upper"))
    print("A is {}".format("lower" if islower("A") else "upper"))
    print("3 is {}".format("lower" if islower("3") else "upper"))
    print("g is {}".format("lower" if islower("g") else "upper"))

    user@ubuntu:~/$ ./7-main.py
    a is lower
    H is upper
    A is upper
    3 is upper
    g is lower
    user@ubuntu:~/$ 
    ```

### 8. 🔠 To Uppercase
Write a function that prints a string in uppercase followed by a new line.

- **File:** `8-uppercase.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 8-main.py
    #!/usr/bin/env python3
    uppercase = __import__('8-uppercase').uppercase

    uppercase("best")
    uppercase("Best School 98 Battery street")

    user@ubuntu:~/$ ./8-main.py
    BEST
    BEST SCHOOL 98 BATTERY STREET
    user@ubuntu:~/$ 
    ```

### 9. 🔢 Print Last Digit
Write a function that prints the last digit of a number.

- **File:** `9-print_last_digit.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 9-main.py
    #!/usr/bin/env python3
    print_last_digit = __import__('9-print_last_digit').print_last_digit

    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)

    user@ubuntu:~/$ ./9-main.py
    8044
    user@ubuntu:~/$ 
    ```

### 10. ➕ Add
Write a function that adds two integers and returns the result.

- **File:** `10-add.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 10-main.py
    #!/usr/bin/env python3
    add = __import__('10-add').add

    print(add(1, 2))
    print(add(98, 0))
    print(add(100, -2))

    user@ubuntu:~/$ ./10-main.py
    3
    98
    98
    user@ubuntu:~/$ 
    ```

### 11. ✖️ Power
Write a function that computes a to the power of b and return the value.

- **File:** `11-pow.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 11-main.py
    #!/usr/bin/env python3
    pow = __import__('11-pow').pow

    print(pow(2, 2))
    print(pow(98, 2))
    print(pow(98, 0))
    print(pow(100, -2))
    print(pow(-4, 5))

    user@ubuntu:~/$ ./11-main.py
    4
    9604
    1
    0.0001
    -1024
    user@ubuntu:~/$ 
    ```

### 12. 🥤 Fizz Buzz
Write a function that prints the numbers from 1 to 100 separated by a space.

- **File:** `12-fizzbuzz.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 12-main.py
    #!/usr/bin/env python3
    fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

    fizzbuzz()
    print("")

    user@ubuntu:~/$ ./12-main.py | cat -e
    1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
    user@ubuntu:~/$ 
    ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-if_else_loops_functions`