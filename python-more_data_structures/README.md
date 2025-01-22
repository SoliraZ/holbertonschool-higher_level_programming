# 📊 Python More Data Structures

This repository contains various Python scripts that demonstrate advanced programming concepts related to data structures.

## 📋 Tasks

### 0. 🟦 Square Matrix Simple
Write a function that computes the square value of all integers of a matrix.

- **File:** `0-square_matrix_simple.py`
- **Prototype:** `def square_matrix_simple(matrix=[]):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 0-main.py
    #!/usr/bin/python3
    square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)

    user@ubuntu:~/$ ./0-main.py
    [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    user@ubuntu:~/$ 
    ```

### 1. 🔄 Search and Replace
Write a function that replaces all occurrences of an element by another in a new list.

- **File:** `1-search_replace.py`
- **Prototype:** `def search_replace(my_list, search, replace):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 1-main.py
    #!/usr/bin/python3
    search_replace = __import__('1-search_replace').search_replace

    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)

    user@ubuntu:~/$ ./1-main.py
    [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
    [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    user@ubuntu:~/$ 
    ```

### 2. ➕ Unique Addition
Write a function that adds all unique integers in a list (only once for each integer).

- **File:** `2-uniq_add.py`
- **Prototype:** `def uniq_add(my_list=[]):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 2-main.py
    #!/usr/bin/python3
    uniq_add = __import__('2-uniq_add').uniq_add

    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))

    user@ubuntu:~/$ ./2-main.py
    Result: 15
    user@ubuntu:~/$ 
    ```

### 3. 🔄 Present in Both
Write a function that returns a set of common elements in two sets.

- **File:** `3-common_elements.py`
- **Prototype:** `def common_elements(set_1, set_2):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 3-main.py
    #!/usr/bin/python3
    common_elements = __import__('3-common_elements').common_elements

    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))

    user@ubuntu:~/$ ./3-main.py
    ['C']
    user@ubuntu:~/$ 
    ```

### 4. 🔄 Only Differents
Write a function that returns a set of all elements present in only one set.

- **File:** `4-only_diff_elements.py`
- **Prototype:** `def only_diff_elements(set_1, set_2):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 4-main.py
    #!/usr/bin/python3
    only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))

    user@ubuntu:~/$ ./4-main.py
    ['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
    user@ubuntu:~/$ 
    ```

### 5. 🔑 Number of Keys
Write a function that returns the number of keys in a dictionary.

- **File:** `5-number_keys.py`
- **Prototype:** `def number_keys(a_dictionary):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 5-main.py
    #!/usr/bin/python3
    number_keys = __import__('5-number_keys').number_keys

    a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))

    user@ubuntu:~/$ ./5-main.py
    Number of keys: 3
    user@ubuntu:~/$ 
    ```

### 6. 🔠 Print Sorted Dictionary
Write a function that prints a dictionary by ordered keys.

- **File:** `6-print_sorted_dictionary.py`
- **Prototype:** `def print_sorted_dictionary(a_dictionary):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 6-main.py
    #!/usr/bin/python3
    print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)

    user@ubuntu:~/$ ./6-main.py
    Number: 89
    ids: [1, 2, 3]
    language: C
    track: Low level
    user@ubuntu:~/$ 
    ```

### 7. 🔄 Update Dictionary
Write a function that replaces or adds key/value in a dictionary.

- **File:** `7-update_dictionary.py`
- **Prototype:** `def update_dictionary(a_dictionary, key, value):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 7-main.py
    #!/usr/bin/python3
    update_dictionary = __import__('7-update_dictionary').update_dictionary
    print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

    print("--")
    print("--")

    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

    user@ubuntu:~/$ ./7-main.py
    language: Python
    number: 89
    track: Low level
    --
    language: Python
    number: 89
    track: Low level
    --
    --
    city: San Francisco
    language: Python
    number: 89
    track: Low level
    --
    city: San Francisco
    language: Python
    number: 89
    track: Low level
    user@ubuntu:~/$ 
    ```

### 8. ❌ Simple Delete by Key
Write a function that deletes a key in a dictionary.

- **File:** `8-simple_delete.py`
- **Prototype:** `def simple_delete(a_dictionary, key=""):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 8-main.py
    #!/usr/bin/python3
    simple_delete = __import__('8-simple_delete').simple_delete
    print_sorted_dictionary = \
        __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
    new_dict = simple_delete(a_dictionary, 'track')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    user@ubuntu:~/$ ./8-main.py
    Number: 89
    ids: [1, 2, 3]
    language: C
    --
    Number: 89
    ids: [1, 2, 3]
    language: C
    --
    --
    Number: 89
    ids: [1, 2, 3]
    language: C
    --
    Number: 89
    ids: [1, 2, 3]
    language: C
    user@ubuntu:~/$ 
    ```

### 9. ✖️ Multiply by 2
Write a function that returns a new dictionary with all values multiplied by 2.

- **File:** `9-multiply_by_2.py`
- **Prototype:** `def multiply_by_2(a_dictionary):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 9-main.py
    #!/usr/bin/python3
    multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
    print_sorted_dictionary = \
        __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    user@ubuntu:~/$ ./9-main.py
    Alex: 8
    Bob: 14
    John: 12
    Mike: 14
    Molly: 16
    --
    Alex: 16
    Bob: 28
    John: 24
    Mike: 28
    Molly: 32
    user@ubuntu:~/$ 
    ```

### 10. 🏆 Best Score
Write a function that returns a key with the biggest integer value.

- **File:** `10-best_score.py`
- **Prototype:** `def best_score(a_dictionary):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 10-main.py
    #!/usr/bin/python3
    best_score = __import__('10-best_score').best_score

    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))

    user@ubuntu:~/$ ./10-main.py
    Best score: Molly
    Best score: None
    user@ubuntu:~/$ 
    ```

### 11. ✖️ Multiply by Using Map
Write a function that returns a list with all values multiplied by a number without using any loops.

- **File:** `11-multiply_list_map.py`
- **Prototype:** `def multiply_list_map(my_list=[], number=0):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 11-main.py
    #!/usr/bin/python3
    multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

    my_list = [1, 2, 3, 4, 6]
    new_list = multiply_list_map(my_list, 4)
    print(new_list)
    print(my_list)

    user@ubuntu:~/$ ./11-main.py
    [4, 8, 12, 16, 24]
    [1, 2, 3, 4, 6]
    user@ubuntu:~/$ 
    ```

### 12. 🏛️ Roman to Integer
Technical interview preparation: Create a function `def roman_to_int(roman_string):` that converts a Roman numeral to an integer.

- **File:** `12-roman_to_int.py`
- **Prototype:** `def roman_to_int(roman_string):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 12-main.py
    #!/usr/bin/python3
    """ Roman to Integer test file
    """
    roman_to_int = __import__('12-roman_to_int').roman_to_int

    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    user@ubuntu:~/$ ./12-main.py
    X = 10
    VII = 7
    IX = 9
    LXXXVII = 87
    DCCVII = 707
    user@ubuntu:~/$ 
    ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-more_data_structures`