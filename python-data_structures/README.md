# 🗃️ Python Data Structures

This repository contains various Python scripts that demonstrate basic programming concepts related to data structures.

## 📋 Tasks

### 0. 🖨️ Print List Integer
Write a function that prints all integers of a list.

- **File:** `0-print_list_integer.py`
- **Prototype:** `def print_list_integer(my_list=[]):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 0-main.py
    #!/usr/bin/python3
    print_list_integer = __import__('0-print_list_integer').print_list_integer

    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)

    user@ubuntu:~/$ ./0-main.py
    1
    2
    3
    4
    5
    user@ubuntu:~/$ 
    ```

### 1. 🔍 Secure Access to an Element in a List
Write a function that retrieves an element from a list.

- **File:** `1-element_at.py`
- **Prototype:** `def element_at(my_list, idx):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 1-main.py
    #!/usr/bin/python3
    element_at = __import__('1-element_at').element_at

    my_list = [1, 2, 3, 4, 5]
    idx = 3
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

    user@ubuntu:~/$ ./1-main.py
    Element at index 3 is 4
    user@ubuntu:~/$ 
    ```

### 2. 🔄 Replace Element
Write a function that replaces an element of a list at a specific position.

- **File:** `2-replace_in_list.py`
- **Prototype:** `def replace_in_list(my_list, idx, element):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 2-main.py
    #!/usr/bin/python3
    replace_in_list = __import__('2-replace_in_list').replace_in_list

    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)

    user@ubuntu:~/$ ./2-main.py
    [1, 2, 3, 9, 5]
    [1, 2, 3, 9, 5]
    user@ubuntu:~/$ 
    ```

### 3. 🔄 Print a List of Integers... in Reverse!
Write a function that prints all integers of a list, in reverse order.

- **File:** `3-print_reversed_list_integer.py`
- **Prototype:** `def print_reversed_list_integer(my_list=[]):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 3-main.py
    #!/usr/bin/python3
    print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)

    user@ubuntu:~/$ ./3-main.py
    5
    4
    3
    2
    1
    user@ubuntu:~/$ 
    ```

### 4. 🔄 Replace in a Copy
Write a function that replaces an element in a list at a specific position without modifying the original list.

- **File:** `4-new_in_list.py`
- **Prototype:** `def new_in_list(my_list, idx, element):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 4-main.py
    #!/usr/bin/python3
    new_in_list = __import__('4-new_in_list').new_in_list

    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)

    user@ubuntu:~/$ ./4-main.py
    [1, 2, 3, 9, 5]
    [1, 2, 3, 4, 5]
    user@ubuntu:~/$ 
    ```

### 5. ❌ Can You C Me Now?
Write a function that removes all characters c and C from a string.

- **File:** `5-no_c.py`
- **Prototype:** `def no_c(my_string):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 5-main.py
    #!/usr/bin/python3
    no_c = __import__('5-no_c').no_c

    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))

    user@ubuntu:~/$ ./5-main.py
    Best Shool
    hiago
     is fun!
    user@ubuntu:~/$ 
    ```

### 6. 🟦 Lists of Lists = Matrix
Write a function that prints a matrix of integers.

- **File:** `6-print_matrix_integer.py`
- **Prototype:** `def print_matrix_integer(matrix=[[]]):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 6-main.py
    #!/usr/bin/python3
    print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()

    user@ubuntu:~/$ ./6-main.py | cat -e
    1 2 3$
    4 5 6$
    7 8 9$
    --$
    $
    user@ubuntu:~/$ 
    ```

### 7. ➕ Tuples Addition
Write a function that adds 2 tuples.

- **File:** `7-add_tuple.py`
- **Prototype:** `def add_tuple(tuple_a=(), tuple_b=()):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 7-main.py
    #!/usr/bin/python3
    add_tuple = __import__('7-add_tuple').add_tuple

    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))

    user@ubuntu:~/$ ./7-main.py
    (89, 100)
    (2, 89)
    (1, 89)
    user@ubuntu:~/$ 
    ```

### 8. 🔄 More Returns!
Write a function that returns a tuple with the length of a string and its first character.

- **File:** `8-multiple_returns.py`
- **Prototype:** `def multiple_returns(sentence):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 8-main.py
    #!/usr/bin/python3
    multiple_returns = __import__('8-multiple_returns').multiple_returns

    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))

    user@ubuntu:~/$ ./8-main.py
    Length: 22 - First character: A
    user@ubuntu:~/$ 
    ```

### 9. 🔍 Find the Max
Write a function that finds the biggest integer of a list.

- **File:** `9-max_integer.py`
- **Prototype:** `def max_integer(my_list=[]):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 9-main.py
    #!/usr/bin/python3
    max_integer = __import__('9-max_integer').max_integer

    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))

    user@ubuntu:~/$ ./9-main.py
    Max: 90
    user@ubuntu:~/$ 
    ```

### 10. ✖️ Only by 2
Write a function that finds all multiples of 2 in a list.

- **File:** `10-divisible_by_2.py`
- **Prototype:** `def divisible_by_2(my_list=[]):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 10-main.py
    #!/usr/bin/python3
    divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1

    user@ubuntu:~/$ ./10-main.py
    0 is divisible by 2
    1 is not divisible by 2
    2 is divisible by 2
    3 is not divisible by 2
    4 is divisible by 2
    5 is not divisible by 2
    6 is divisible by 2
    user@ubuntu:~/$ 
    ```

### 11. ❌ Delete at
Write a function that deletes the item at a specific position in a list.

- **File:** `11-delete_at.py`
- **Prototype:** `def delete_at(my_list=[], idx=0):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 11-main.py
    #!/usr/bin/python3
    delete_at = __import__('11-delete_at').delete_at

    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)

    user@ubuntu:~/$ ./11-main.py
    [1, 2, 3, 5]
    [1, 2, 3, 5]
    user@ubuntu:~/$ 
    ```

### 12. 🔄 Switch
Complete the source code in order to switch value of a and b.

- **File:** `12-switch.py`
- **Usage:**
    ```sh
    user@ubuntu:~/py/$ ./12-switch.py
    a=10 - b=89
    user@ubuntu:~/py/$ wc -l 12-switch.py
    5 12-switch.py
    user@ubuntu:~/py/$ 
    ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-data_structures`