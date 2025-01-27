# 🚨 Python Exceptions

This repository contains various Python scripts that demonstrate basic programming concepts related to exception handling.

## 📋 Tasks

### 0. 🖨️ Safe Print List
Write a function that prints x elements of a list.

- **File:** `0-safe_print_list.py`
- **Prototype:** `def safe_print_list(my_list=[], x=0):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 0-main.py
    #!/usr/bin/python3
    safe_print_list = __import__('0-safe_print_list').safe_print_list

    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))

    user@ubuntu:~/$ ./0-main.py
    12
    nb_print: 2
    12345
    nb_print: 5
    12345
    nb_print: 5
    user@ubuntu:~/$ 
    ```

### 1. 🔢 Safe Printing of an Integers List
Write a function that prints an integer with `"{:d}".format()`.

- **File:** `1-safe_print_integer.py`
- **Prototype:** `def safe_print_integer(value):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 1-main.py
    #!/usr/bin/python3
    safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

    value = 89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    user@ubuntu:~/$ ./1-main.py
    89
    -89
    School is not an integer
    user@ubuntu:~/$ 
    ```

### 2. 🔢 Print and Count Integers
Write a function that prints the first x elements of a list and only integers.

- **File:** `2-safe_print_list_integers.py`
- **Prototype:** `def safe_print_list_integers(my_list=[], x=0):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 2-main.py
    #!/usr/bin/python3
    safe_print_list_integers = \
        __import__('2-safe_print_list_integers').safe_print_list_integers

    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))

    user@ubuntu:~/$ ./2-main.py
    12
    nb_print: 2
    12345
    nb_print: 5
    12345Traceback (most recent call last):
      File "./2-main.py", line 14, in <module>
        nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
      File "//2-safe_print_list_integers.py", line 7, in safe_print_list_integers
        print("{:d}".format(my_list[i]), end="")
    IndexError: list index out of range
    user@ubuntu:~/$ 
    ```

### 3. ➗ Integers Division with Debug
Write a function that divides 2 integers and prints the result.

- **File:** `3-safe_print_division.py`
- **Prototype:** `def safe_print_division(a, b):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 3-main.py
    #!/usr/bin/python3
    safe_print_division = __import__('3-safe_print_division').safe_print_division

    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    user@ubuntu:~/$ ./3-main.py
    Inside result: 6.0
    12 / 2 = 6.0
    Inside result: None
    12 / 0 = None
    user@ubuntu:~/$ 
    ```

### 4. ➗ Divide a List
Write a function that divides element by element 2 lists.

- **File:** `4-list_division.py`
- **Prototype:** `def list_division(my_list_1, my_list_2, list_length):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 4-main.py
    #!/usr/bin/python3
    list_division = __import__('4-list_division').list_division

    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    user@ubuntu:~/$ ./4-main.py
    [5.0, 2.0, 1.0]
    --
    division by 0
    wrong type
    out of range
    [5.0, 0, 0, 2.0, 0]
    user@ubuntu:~/$ 
    ```

### 5. 🚨 Raise Exception
Write a function that raises a type exception.

- **File:** `5-raise_exception.py`
- **Prototype:** `def raise_exception():`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 5-main.py
    #!/usr/bin/python3
    raise_exception = __import__('5-raise_exception').raise_exception

    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")

    user@ubuntu:~/$ ./5-main.py
    Exception raised
    user@ubuntu:~/$ 
    ```

### 6. 🚨 Raise a Message
Write a function that raises a name exception with a message.

- **File:** `6-raise_exception_msg.py`
- **Prototype:** `def raise_exception_msg(message=""):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 6-main.py
    #!/usr/bin/python3
    raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)

    user@ubuntu:~/$ ./6-main.py
    C is fun
    user@ubuntu:~/$ 
    ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-exceptions`