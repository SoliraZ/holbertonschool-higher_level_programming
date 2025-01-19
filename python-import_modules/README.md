# 📦 Python Import Modules

This repository contains various Python scripts that demonstrate basic programming concepts related to importing modules and functions.

## 📋 Tasks

### 0. ➕ Import a Simple Function from a Simple File
Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

- **File:** `0-add.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ ./0-add.py
    1 + 2 = 3
    user@ubuntu:~/$ 
    ```

### 1. 🛠️ My First Toolbox!
Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.

- **File:** `1-calculation.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ ./1-calculation.py
    10 + 5 = 15
    10 - 5 = 5
    10 * 5 = 50
    10 / 5 = 2
    user@ubuntu:~/$ 
    ```

### 2. 🧮 How to Make a Script Dynamic!
Write a program that prints the number of and the list of its arguments.

- **File:** `2-args.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ ./2-args.py 
    0 arguments.
    user@ubuntu:~/$ ./2-args.py Hello
    1 argument:
    1: Hello
    user@ubuntu:~/$ ./2-args.py Hello Welcome To The Best School
    6 arguments:
    1: Hello
    2: Welcome
    3: To
    4: The
    5: Best
    6: School
    user@ubuntu:~/$ 
    ```

### 3. ➕ Infinite Addition
Write a program that prints the result of the addition of all arguments.

- **File:** `3-infinite_add.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ ./3-infinite_add.py
    0
    user@ubuntu:~/$ ./3-infinite_add.py 79 10
    89
    user@ubuntu:~/$ ./3-infinite_add.py 79 10 -40 -300 89 
    -162
    user@ubuntu:~/$ 
    ```

### 4. 👀 Who Are You?
Write a program that prints all the names defined by the compiled module `hidden_4.pyc`.

- **File:** `4-hidden_discovery.py`
- **Usage:**
    ```sh
    user@ubuntu:/tmp$ ./4-hidden_discovery.py | sort
    my_secret_santa
    print_hidden
    print_school
    user@ubuntu:/tmp$ 
    ```

### 5. 📦 Everything Can Be Imported
Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

- **File:** `5-variable_load.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ ./5-variable_load.py
    98
    user@ubuntu:~/$ 
    ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-import_modules`
