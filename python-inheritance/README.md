# 🧬 Python Inheritance

This repository contains various Python scripts that demonstrate basic programming concepts related to inheritance.

## 📋 Tasks

### 0. 🔍 Lookup
Write a function that returns the list of available attributes and methods of an object.

- **File:** `0-lookup.py`
- **Prototype:** `def lookup(obj):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 0-main.py
    #!/usr/bin/python3
    lookup = __import__('0-lookup').lookup

    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3
        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))

    user@ubuntu:~/$ ./0-main.py
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
    ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
    user@ubuntu:~/$ 
    ```

### 1. 📋 My List
Write a class MyList that inherits from list.

- **File:** `1-my_list.py`, `tests/1-my_list.txt`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 1-main.py
    #!/usr/bin/python3
    MyList = __import__('1-my_list').MyList

    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)

    user@ubuntu:~/$ ./1-main.py
    [1, 4, 2, 3, 5]
    [1, 2, 3, 4, 5]
    [1, 4, 2, 3, 5]
    user@ubuntu:~/$ 
    ```

### 2. ✅ Exact Same Object
Write a function that returns True if the object is exactly an instance of the specified class; otherwise False.

- **File:** `2-is_same_class.py`
- **Prototype:** `def is_same_class(obj, a_class):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 2-main.py
    #!/usr/bin/python3
    is_same_class = __import__('2-is_same_class').is_same_class

    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))

    user@ubuntu:~/$ ./2-main.py
    1 is an instance of the class int
    user@ubuntu:~/$ 
    ```

### 3. 🧬 Same Class or Inherit From
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.

- **File:** `3-is_kind_of_class.py`
- **Prototype:** `def is_kind_of_class(obj, a_class):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 3-main.py
    #!/usr/bin/python3
    is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))

    user@ubuntu:~/$ ./3-main.py
    1 comes from int
    1 comes from object
    user@ubuntu:~/$ 
    ```

### 4. 🧬 Only Subclass of
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.

- **File:** `4-inherits_from.py`
- **Prototype:** `def inherits_from(obj, a_class):`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 4-main.py
    #!/usr/bin/python3
    inherits_from = __import__('4-inherits_from').inherits_from

    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))

    user@ubuntu:~/$ ./4-main.py
    True inherited from class int
    True inherited from class object
    user@ubuntu:~/$ 
    ```

### 5. 📐 Geometry Module
Write an empty class BaseGeometry.

- **File:** `5-base_geometry.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 5-main.py
    #!/usr/bin/python3
    BaseGeometry = __import__('5-base_geometry').BaseGeometry

    bg = BaseGeometry()

    print(bg)
    print(dir(bg))
    print(dir(BaseGeometry))

    user@ubuntu:~/$ ./5-main.py
    <5-base_geometry.BaseGeometry object at 0x7f2050c69208>
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
    user@ubuntu:~/$ 
    ```

### 6. 📐 Improve Geometry
Write a class BaseGeometry (based on `5-base_geometry.py`).

- **File:** `6-base_geometry.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 6-main.py
    #!/usr/bin/python3
    BaseGeometry = __import__('6-base_geometry').BaseGeometry

    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    user@ubuntu:~/$ ./6-main.py
    [Exception] area() is not implemented
    user@ubuntu:~/$ 
    ```

### 7. 📐 Integer Validator
Write a class BaseGeometry (based on `6-base_geometry.py`).

- **File:** `7-base_geometry.py`, `tests/7-base_geometry.txt`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 7-main.py
    #!/usr/bin/python3
    BaseGeometry = __import__('7-base_geometry').BaseGeometry

    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    user@ubuntu:~/$ ./7-main.py
    [TypeError] name must be an integer
    [ValueError] age must be greater than 0
    [ValueError] distance must be greater than 0
    user@ubuntu:~/$ 
    ```

### 8. 🟦 Rectangle
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

- **File:** `8-rectangle.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 8-main.py
    #!/usr/bin/python3
    Rectangle = __import__('8-rectangle').Rectangle

    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    user@ubuntu:~/$ ./8-main.py
    <8-rectangle.Rectangle object at 0x7f6f488f7eb8>
    ['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
    [AttributeError] 'Rectangle' object has no attribute 'width'
    [TypeError] height must be an integer
    user@ubuntu:~/$ 
    ```

### 9. 🟦 Full Rectangle
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on `8-rectangle.py`)

- **File:** `9-rectangle.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 9-main.py
    #!/usr/bin/python3
    Rectangle = __import__('9-rectangle').Rectangle

    r = Rectangle(3, 5)

    print(r)
    print(r.area())

    user@ubuntu:~/$ ./9-main.py
    [Rectangle] 3/5
    15
    user@ubuntu:~/$ 
    ```

### 10. 🟦 Square #1
Write a class Square that inherits from Rectangle (9-rectangle.py).

- **File:** `10-square.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 10-main.py
    #!/usr/bin/python3
    Square = __import__('10-square').Square

    s = Square(13)

    print(s)
    print(s.area())

    user@ubuntu:~/$ ./10-main.py
    [Rectangle] 13/13
    169
    user@ubuntu:~/$ 
    ```

### 11. 🟦 Square #2
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on `10-square.py`).

- **File:** `11-square.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 11-main.py
    #!/usr/bin/python3
    Square = __import__('11-square').Square

    s = Square(13)

    print(s)
    print(s.area())

    user@ubuntu:~/$ ./11-main.py
    [Square] 13/13
    169
    user@ubuntu:~/$ 
    ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-inheritance`