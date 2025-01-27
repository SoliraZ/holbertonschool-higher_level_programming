# 🟦 Python Classes

This repository contains various Python scripts that demonstrate basic programming concepts related to classes and objects.

## 📋 Tasks

### 0. 🟦 Square
Write an empty class Square that defines a square.

- **File:** `0-square.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 0-main.py
    #!/usr/bin/python3
    Square = __import__('0-square').Square

    my_square = Square()
    print(type(my_square))
    print(my_square.__dict__)

    user@ubuntu:~/$ ./0-main.py
    <class '0-square.Square'>
    {}
    user@ubuntu:~/$ 
    ```

### 1. 🟦 Square with Size
Write a class Square that defines a square by: (based on `0-square.py`)

- **File:** `1-square.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 1-main.py
    #!/usr/bin/python3
    Square = __import__('1-square').Square

    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)

    user@ubuntu:~/$ ./1-main.py
    <class '1-square.Square'>
    {'_Square__size': 3}
    'Square' object has no attribute 'size'
    'Square' object has no attribute '__size'
    user@ubuntu:~/$ 
    ```

### 2. 🟦 Size Validation
Write a class Square that defines a square by: (based on `1-square.py`)

- **File:** `2-square.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 2-main.py
    #!/usr/bin/python3
    Square = __import__('2-square').Square

    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    try:
        my_square_3 = Square("3")
        print(type(my_square_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(-89)
        print(type(my_square_4))
        print(my_square_4.__dict__)
    except Exception as e:
        print(e)

    user@ubuntu:~/$ ./2-main.py
    <class '2-square.Square'>
    {'_Square__size': 3}
    <class '2-square.Square'>
    {'_Square__size': 0}
    'Square' object has no attribute 'size'
    'Square' object has no attribute '__size'
    size must be an integer
    size must be >= 0
    user@ubuntu:~/$ 
    ```

### 3. 🟦 Area of a Square
Write a class Square that defines a square by: (based on `2-square.py`)

- **File:** `3-square.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 3-main.py
    #!/usr/bin/python3
    Square = __import__('3-square').Square

    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))

    user@ubuntu:~/$ ./3-main.py
    Area: 9
    'Square' object has no attribute 'size'
    'Square' object has no attribute '__size'
    Area: 25
    user@ubuntu:~/$ 
    ```

### 4. 🟦 Access and Update Private Attribute
Write a class Square that defines a square by: (based on `3-square.py`)

- **File:** `4-square.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 4-main.py
    #!/usr/bin/python3
    Square = __import__('4-square').Square

    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)

    user@ubuntu:~/$ ./4-main.py
    Area: 7921 for size: 89
    Area: 9 for size: 3
    size must be an integer
    user@ubuntu:~/$ 
    ```

### 5. 🟦 Printing a Square
Write a class Square that defines a square by: (based on `4-square.py`)

- **File:** `5-square.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 5-main.py
    #!/usr/bin/python3
    Square = __import__('5-square').Square

    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")

    user@ubuntu:~/$ ./5-main.py
    ###
    ###
    ###
    --
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
    --
    --
    user@ubuntu:~/$ 
    ```

### 6. 🟦 Coordinates of a Square
Write a class Square that defines a square by: (based on `5-square.py`)

- **File:** `6-square.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 6-main.py
    #!/usr/bin/python3
    Square = __import__('6-square').Square

    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")

    user@ubuntu:~/$ ./6-main.py | tr " " "_" | cat -e
    ###$
    ###$
    ###$
    --$
    $
    _###$
    _###$
    _###$
    --$
    ___###$
    ___###$
    ___###$
    --$
    user@ubuntu:~/$ 
    ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-classes`