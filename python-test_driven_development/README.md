# 🧪 Python Test-Driven Development

This repository contains various Python scripts that demonstrate basic programming concepts related to test-driven development.

## 📋 Tasks

### 0. ➕ Add Integer
Write a function that adds 2 integers.

- **File:** `0-add_integer.py`, `tests/0-add_integer.txt`
- **Prototype:** `def add_integer(a, b=98):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 0-main.py
    #!/usr/bin/python3
    add_integer = __import__('0-add_integer').add_integer

    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)

    user@ubuntu:~/$ ./0-main.py
    3
    98
    100
    98
    b must be an integer
    a must be an integer
    user@ubuntu:~/$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
    9 passed and 0 failed.
    Test passed.
    user@ubuntu:~/$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
    5
    user@ubuntu:~/$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
    3
    user@ubuntu:~/$ 
    ```

### 1. ➗ Divide a Matrix
Write a function that divides all elements of a matrix.

- **File:** `2-matrix_divided.py`, `tests/2-matrix_divided.txt`
- **Prototype:** `def matrix_divided(matrix, div):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 2-main.py
    #!/usr/bin/python3
    matrix_divided = __import__('2-matrix_divided').matrix_divided

    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)

    user@ubuntu:~/$ ./2-main.py
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    [[1, 2, 3], [4, 5, 6]]
    user@ubuntu:~/$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
    5 passed and 0 failed.
    Test passed.
    user@ubuntu:~/$ 
    ```

### 2. 🗣️ Say My Name
Write a function that prints My name is `<first name> <last name>`.

- **File:** `3-say_my_name.py`, `tests/3-say_my_name.txt`
- **Prototype:** `def say_my_name(first_name, last_name=""):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 3-main.py
    #!/usr/bin/python3
    say_my_name = __import__('3-say_my_name').say_my_name

    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)

    user@ubuntu:~/$ ./3-main.py | cat -e
    My name is John Smith$
    My name is Walter White$
    My name is Bob $
    first_name must be a string$
    user@ubuntu:~/$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
    5 passed and 0 failed.
    Test passed.
    user@ubuntu:~/$ 
    ```

### 3. 🟦 Print Square
Write a function that prints a square with the character `#`.

- **File:** `4-print_square.py`, `tests/4-print_square.txt`
- **Prototype:** `def print_square(size):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 4-main.py
    #!/usr/bin/python3
    print_square = __import__('4-print_square').print_square

    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")

    user@ubuntu:~/$ ./4-main.py
    ####
    ####
    ####
    ####

    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########


    #

    size must be >= 0

    user@ubuntu:~/$ python3 -m doctest -v ./tests/4-print_square.txt
    user@ubuntu:~/$ 
    ```

### 4. 📝 Text Indentation
Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`.

- **File:** `5-text_indentation.py`, `tests/5-text_indentation.txt`
- **Prototype:** `def text_indentation(text):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 5-main.py
    #!/usr/bin/python3
    text_indentation = __import__('5-text_indentation').text_indentation

    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres""")

    user@ubuntu:~/$ ./5-main.py | cat -e
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
    $
    Quonam modo?$
    $
    Utrum igitur tibi litteram videor an totas paginas commovere?$
    $
    Non autem hoc:$
    $
    igitur ne illud quidem.$
    $
    Fortasse id optimum, sed ubi illud:$
    $
    Plus semper voluptatis?$
    $
    Teneo, inquit, finem illi videri nihil dolere.$
    $
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
    $
    Si id dicis, vicimus.$
    $
    Inde sermone vario sex illa a Dipylo stadia confecimus.$
    $
    Sin aliud quid voles, postea.$
    $
    Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
    $
    Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/$
    user@ubuntu:~/$ python3 -m doctest -v ./tests/5-text_indentation.txt
    user@ubuntu:~/$ 
    ```

### 5. 🧪 Max Integer - Unittest
Write unittests for the function `def max_integer(list=[]):`.

- **File:** `tests/6-max_integer_test.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 6-max_integer.py
    #!/usr/bin/python3
    """Module to find the max integer in a list
    """

    def max_integer(list=[]):
        """Function to find and return the max integer in a list of integers
            If the list is empty, the function returns None
        """
        if len(list) == 0:
            return None
        result = list[0]
        i = 1
        while i < len(list):
            if list[i] > result:
                result = list[i]
            i += 1
        return result

    user@ubuntu:~/$ 
    user@ubuntu:~/$ cat 6-main.py
    #!/usr/bin/python3
    max_integer = __import__('6-max_integer').max_integer

    print(max_integer([1, 2, 3, 4]))
    print(max_integer([1, 3, 4, 2]))
    user@ubuntu:~/$
    user@ubuntu:~/$ ./6-main.py
    4
    4
    user@ubuntu:~/$
    user@ubuntu:~/$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
    OK
    user@ubuntu:~/$
    user@ubuntu:~/$ head -7 tests/6-max_integer_test.py 
    #!/usr/bin/python3
    """Unittest for max_integer([..])
    """
    import unittest
    max_integer = __import__('6-max_integer').max_integer

    class TestMaxInteger(unittest.TestCase):
    user@ubuntu:~/$ 
    ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-test_driven_development`