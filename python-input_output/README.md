# 📂 Python Input/Output

This repository contains various Python scripts that demonstrate basic programming concepts related to file input and output operations.

## 📋 Tasks

### 0. 📖 Read File
Write a function that reads a text file (UTF8) and prints it to stdout.

- **Prototype:** `def read_file(filename=""):`
- **File:** `0-read_file.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 0-main.py
    #!/usr/bin/python3
    read_file = __import__('0-read_file').read_file

    read_file("my_file_0.txt")

    user@ubuntu:~/$ cat my_file_0.txt
    We offer a truly innovative approach to education:
    focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

    A school every software engineer would have dreamt of!
    user@ubuntu:~/$ ./0-main.py
    We offer a truly innovative approach to education:
    focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

    A school every software engineer would have dreamt of!
    user@ubuntu:~/$ 
    ```

### 1. ✍️ Write to a File
Write a function that writes a string to a text file (UTF8) and returns the number of characters written.

- **Prototype:** `def write_file(filename="", text=""):`
- **File:** `1-write_file.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 1-main.py
    #!/usr/bin/python3
    write_file = __import__('1-write_file').write_file

    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)

    user@ubuntu:~/$ ./1-main.py
    24
    user@ubuntu:~/$ cat my_first_file.txt
    This School is so cool!
    user@ubuntu:~/$ 
    ```

### 2. 📥 Append to a File
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.

- **Prototype:** `def append_write(filename="", text=""):`
- **File:** `2-append_write.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 2-main.py
    #!/usr/bin/python3
    append_write = __import__('2-append_write').append_write

    nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)

    user@ubuntu:~/$ cat file_append.txt
    This School is so cool!
    user@ubuntu:~/$ ./2-main.py
    24
    user@ubuntu:~/$ cat file_append.txt
    This School is so cool!
    This School is so cool!
    user@ubuntu:~/$ 
    ```

### 3. 🔄 To JSON String
Write a function that returns the JSON representation of an object (string).

- **Prototype:** `def to_json_string(my_obj):`
- **File:** `3-to_json_string.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 3-main.py
    #!/usr/bin/python3
    to_json_string = __import__('3-to_json_string').to_json_string

    my_list = [1, 2, 3]
    s_my_list = to_json_string(my_list)
    print(s_my_list)
    print(type(s_my_list))

    my_dict = { 
        'id': 12,
        'name': "John",
        'places': [ "San Francisco", "Tokyo" ],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    s_my_dict = to_json_string(my_dict)
    print(s_my_dict)
    print(type(s_my_dict))

    try:
        my_set = { 132, 3 }
        s_my_set = to_json_string(my_set)
        print(s_my_set)
        print(type(s_my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    user@ubuntu:~/$ ./3-main.py
    [1, 2, 3]
    <class 'str'>
    {"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": true, "info": {"age": 36, "average": 3.14}}
    <class 'str'>
    [TypeError] Object of type set is not JSON serializable
    user@ubuntu:~/$ 
    ```

### 4. 🔄 From JSON String to Object
Write a function that returns an object (Python data structure) represented by a JSON string.

- **Prototype:** `def from_json_string(my_str):`
- **File:** `4-from_json_string.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 4-main.py
    #!/usr/bin/python3
    from_json_string = __import__('4-from_json_string').from_json_string

    s_my_list = "[1, 2, 3]"
    my_list = from_json_string(s_my_list)
    print(my_list)
    print(type(my_list))

    s_my_dict = """
    {"is_active": true, "info": {"age": 36, "average": 3.14}, 
    "id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))

    try:
        s_my_dict = """
        {"is_active": true, 12 }
        """
        my_dict = from_json_string(s_my_dict)
        print(my_dict)
        print(type(my_dict))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    user@ubuntu:~/$ ./4-main.py
    [1, 2, 3]
    <class 'list'>
    {'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
    <class 'dict'>
    [JSONDecodeError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
    user@ubuntu:~/$ 
    ```

### 5. 💾 Save Object to a File
Write a function that writes an Object to a text file, using a JSON representation.

- **Prototype:** `def save_to_json_file(my_obj, filename):`
- **File:** `5-save_to_json_file.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 5-main.py
    #!/usr/bin/python3
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)

    filename = "my_dict.json"
    my_dict = { 
        'id': 12,
        'name': "John",
        'places': [ "San Francisco", "Tokyo" ],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, filename)

    try:
        filename = "my_set.json"
        my_set = { 132, 3 }
        save_to_json_file(my_set, filename)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    user@ubuntu:~/$ ./5-main.py
    [TypeError] Object of type set is not JSON serializable
    user@ubuntu:~/$ cat my_list.json ; echo ""
    [1, 2, 3]
    user@ubuntu:~/$ cat my_dict.json ; echo ""
    {"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
    user@ubuntu:~/$ cat my_set.json ; echo ""

    user@ubuntu:~/$ 
    ```

### 6. 📂 Create Object from a JSON File
Write a function that creates an Object from a “JSON file”.

- **Prototype:** `def load_from_json_file(filename):`
- **File:** `6-load_from_json_file.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat my_fake.json
    {"is_active": true, 12 }
    user@ubuntu:~/$ cat 6-main.py
    #!/usr/bin/python3
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

    filename = "my_dict.json"
    my_dict = load_from_json_file(filename)
    print(my_dict)
    print(type(my_dict))

    try:
        filename = "my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename)
        print(my_set)
        print(type(my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        filename = "my_fake.json"
        my_fake = load_from_json_file(filename)
        print(my_fake)
        print(type(my_fake))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    user@ubuntu:~/$ cat my_list.json ; echo ""
    [1, 2, 3]
    user@ubuntu:~/$ cat my_dict.json ; echo ""
    {"name": "John", "info": {"age": 36, "average": 3.14}, "id": 12, "places": ["San Francisco", "Tokyo"], "is_active": true}
    user@ubuntu:~/$ cat my_fake.json ; echo ""
    {"is_active": true, 12 }
    user@ubuntu:~/$ ./6-main.py
    [1, 2, 3]
    <class 'list'>
    {'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active': True}
    <class 'dict'>
    [FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
    [JSONDecodeError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
    user@ubuntu:~/$ 
    ```

### 7. ➕ Load, Add, Save
Write a script that adds all arguments to a Python list, and then save them to a file.

- **File:** `7-add_item.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat add_item.json
    cat: add_item.json: No such file or directory
    user@ubuntu:~/$ ./7-add_item.py
    user@ubuntu:~/$ cat add_item.json ; echo ""
    []
    user@ubuntu:~/$ ./7-add_item.py Best School
    user@ubuntu:~/$ cat add_item.json ; echo ""
    ["Best", "School"]
    user@ubuntu:~/$ ./7-add_item.py 89 Python C
    user@ubuntu:~/$ cat add_item.json ; echo ""
    ["Best", "School", "89", "Python", "C"]
    user@ubuntu:~/$ 
    ```

### 8. 🏫 Class to JSON
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.

- **Prototype:** `def class_to_json(obj):`
- **File:** `8-class_to_json.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 8-my_class.py 
    #!/usr/bin/python3
    """ My class module
    """

    class MyClass:
        """ My class
        """

        def __init__(self, name):
            self.name = name
            self.number = 0

        def __str__(self):
            return "[MyClass] {} - {:d}".format(self.name, self.number)

    user@ubuntu:~/$ cat 8-main.py 
    #!/usr/bin/python3
    MyClass = __import__('8-my_class').MyClass
    class_to_json = __import__('8-class_to_json').class_to_json

    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)

    user@ubuntu:~/$ ./8-main.py 
    <class '8-my_class.MyClass'>
    [MyClass] John - 89
    <class 'dict'>
    {'name': 'John', 'number': 89}
    user@ubuntu:~/$ 
    user@ubuntu:~/$ cat 8-my_class_2.py 
    #!/usr/bin/python3
    """ My class module
    """

    class MyClass:
        """ My class
        """

        score = 0

        def __init__(self, name, number = 4):
            self.__name = name
            self.number = number
            self.is_team_red = (self.number % 2) == 0

        def win(self):
            self.score += 1

        def lose(self):
            self.score -= 1

        def __str__(self):
            return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)

    user@ubuntu:~/$ cat 8-main_2.py 
    #!/usr/bin/python3
    MyClass = __import__('8-my_class_2').MyClass
    class_to_json = __import__('8-class_to_json').class_to_json

    m = MyClass("John")
    m.win()
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)

    user@ubuntu:~/$ ./8-main_2.py 
    <class '8-my_class_2.MyClass'>
    [MyClass] John - 4 => 1
    <class 'dict'>
    {'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}
    user@ubuntu:~/$
    ```

### 9. 👨‍🎓 Student to JSON
Write a class Student that defines a student by:

- **Public instance attributes:**
  - `first_name`
  - `last_name`
  - `age`
- **Instantiation with first_name, last_name and age:** `def __init__(self, first_name, last_name, age):`
- **Public method `def to_json(self):` that retrieves a dictionary representation of a Student instance (same as `8-class_to_json.py`)**
- **File:** `9-student.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 9-main.py 
    #!/usr/bin/python3
    Student = __import__('9-student').Student

    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))

    user@ubuntu:~/$ ./9-main.py 
    <class 'dict'>
    John
    <class 'str'>
    23
    <class 'int'>
    <class 'dict'>
    Bob
    <class 'str'>
    27
    <class 'int'>
    user@ubuntu:~/$ 
    ```

### 10. 👨‍🎓 Student to JSON with Filter
Write a class Student that defines a student by: (based on `9-student.py`)

- **Public instance attributes:**
  - `first_name`
  - `last_name`
  - `age`
- **Instantiation with first_name, last_name and age:** `def __init__(self, first_name, last_name, age):`
- **Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance (same as `8-class_to_json.py`):**
  - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
  - Otherwise, all attributes must be retrieved.
- **File:** `10-student.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 10-main.py 
    #!/usr/bin/python3
    Student = __import__('10-student').Student

    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)

    user@ubuntu:~/$ ./10-main.py 
    {'age': 23, 'last_name': 'Doe', 'first_name': 'John'}
    {'age': 27, 'first_name': 'Bob'}
    {'age': 27}
    user@ubuntu:~/$
    ```

    ### 11. 🔄 Student to JSON and Reload
    Write a class Student that defines a student by: (based on `10-student.py`)

    - **Public instance attributes:**
        - `first_name`
        - `last_name`
        - `age`
    - **Instantiation with first_name, last_name and age:** `def __init__(self, first_name, last_name, age):`
    - **Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance (same as `8-class_to_json.py`):**
        - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
        - Otherwise, all attributes must be retrieved.
    - **Public method `def reload_from_json(self, json):` that replaces all attributes of the Student instance:**
        - You can assume `json` will always be a dictionary.
        - A dictionary key will be the public attribute name.
        - A dictionary value will be the value of the public attribute.
    - **File:** `11-student.py`
    - **Usage:**
            ```sh
            guillaume@ubuntu:~/$ cat 11-main.py 
            #!/usr/bin/python3
            import os
            import sys

            Student = __import__('11-student').Student
            read_file = __import__('0-read_file').read_file
            save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
            load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

            path = sys.argv[1]

            if os.path.exists(path):
                    os.remove(path)

            student_1 = Student("John", "Doe", 23)
            j_student_1 = student_1.to_json()
            print("Initial student:")
            print(student_1)
            print(type(student_1))
            print(type(j_student_1))
            print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))

            save_to_json_file(j_student_1, path)
            read_file(path)
            print("\nSaved to disk")

            print("Fake student:")
            new_student_1 = Student("Fake", "Fake", 89)
            print(new_student_1)
            print(type(new_student_1))
            print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

            print("Load dictionary from file:")
            new_j_student_1 = load_from_json_file(path)

            new_student_1.reload_from_json(j_student_1)
            print(new_student_1)
            print(type(new_student_1))
            print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

            guillaume@ubuntu:~/$ ./11-main.py student.json
            Initial student:
            <11-student.Student object at 0x7f832826eda0>
            <class '11-student.Student'>
            <class 'dict'>
            John Doe 23
            {"last_name": "Doe", "first_name": "John", "age": 23}
            Saved to disk
            Fake student:
            <11-student.Student object at 0x7f832826edd8>
            <class '11-student.Student'>
            Fake Fake 89
            Load dictionary from file:
            <11-student.Student object at 0x7f832826edd8>
            <class '11-student.Student'>
            John Doe 23
            guillaume@ubuntu:~/$ cat student.json ; echo ""
            {"last_name": "Doe", "first_name": "John", "age": 23}
            guillaume@ubuntu:~/$ 
            ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-input_output`