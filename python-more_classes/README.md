# 🟦 Python More Classes

This repository contains various Python scripts that demonstrate advanced programming concepts related to classes and objects.

## 📋 Tasks

### 0. 🟦 Rectangle
Write an empty class Rectangle that defines a rectangle.

- **File:** `0-rectangle.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 0-main.py
    #!/usr/bin/python3
    Rectangle = __import__('0-rectangle').Rectangle

    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)

    user@ubuntu:~/$ ./0-main.py
    <class '0-rectangle.Rectangle'>
    {}
    user@ubuntu:~/$ 
    ```

### 1. 🟦 Real Definition of a Rectangle
Write a class Rectangle that defines a rectangle by: (based on `0-rectangle.py`)

- **File:** `1-rectangle.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 1-main.py
    #!/usr/bin/python3
    Rectangle = __import__('1-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)

    user@ubuntu:~/$ ./1-main.py
    {'_Rectangle__width': 2, '_Rectangle__height': 4}
    {'_Rectangle__width': 10, '_Rectangle__height': 3}
    user@ubuntu:~/$ 
    ```

### 2. 🟦 Area and Perimeter
Write a class Rectangle that defines a rectangle by: (based on `1-rectangle.py`)

- **File:** `2-rectangle.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 2-main.py
    #!/usr/bin/python3
    Rectangle = __import__('2-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    user@ubuntu:~/$ ./2-main.py
    Area: 8 - Perimeter: 12
    --
    Area: 30 - Perimeter: 26
    user@ubuntu:~/$ 
    ```

### 3. 🟦 String Representation
Write a class Rectangle that defines a rectangle by: (based on `2-rectangle.py`)

- **File:** `3-rectangle.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 3-main.py
    #!/usr/bin/python3
    Rectangle = __import__('3-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)
    print(repr(my_rectangle))

    user@ubuntu:~/$ ./3-main.py
    Area: 8 - Perimeter: 12
    ##
    ##
    ##
    ##
    <3-rectangle.Rectangle object at 0x7f92a75a2eb8>
    --
    ##########
    ##########
    ##########
    <3-rectangle.Rectangle object at 0x7f92a75a2eb8>
    user@ubuntu:~/$ 
    ```

### 4. 🟦 Eval is Magic
Write a class Rectangle that defines a rectangle by: (based on `3-rectangle.py`)

- **File:** `4-rectangle.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 4-main.py
    #!/usr/bin/python3
    Rectangle = __import__('4-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))

    user@ubuntu:~/$ ./4-main.py
    ##
    ##
    ##
    ##
    --
    ##
    ##
    ##
    ##
    --
    Rectangle(2, 4)
    --
    0x7f09ebf7cc88
    --
    ##
    ##
    ##
    ##
    --
    ##
    ##
    ##
    ##
    --
    Rectangle(2, 4)
    --
    0x7f09ebf7ccc0
    --
    False
    True
    user@ubuntu:~/$ 
    ```

### 5. 🟦 Detect Instance Deletion
Write a class Rectangle that defines a rectangle by: (based on `4-rectangle.py`)

- **File:** `5-rectangle.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 5-main.py
    #!/usr/bin/python3
    Rectangle = __import__('5-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    del my_rectangle

    try:
        print(my_rectangle)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    user@ubuntu:~/$ ./5-main.py
    Area: 8 - Perimeter: 12
    Bye rectangle...
    [NameError] name 'my_rectangle' is not defined
    user@ubuntu:~/$ 
    ```

### 6. 🟦 How Many Instances
Write a class Rectangle that defines a rectangle by: (based on `5-rectangle.py`)

- **File:** `6-rectangle.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 6-main.py
    #!/usr/bin/python3
    Rectangle = __import__('6-rectangle').Rectangle

    my_rectangle_1 = Rectangle(2, 4)
    my_rectangle_2 = Rectangle(2, 4)
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
    del my_rectangle_1
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
    del my_rectangle_2
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

    user@ubuntu:~/$ ./6-main.py
    2 instances of Rectangle
    Bye rectangle...
    1 instances of Rectangle
    Bye rectangle...
    0 instances of Rectangle
    user@ubuntu:~/$ 
    ```

### 7. 🟦 Change Representation
Write a class Rectangle that defines a rectangle by: (based on `6-rectangle.py`)

- **File:** `7-rectangle.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 7-main.py
    #!/usr/bin/python3
    Rectangle = __import__('7-rectangle').Rectangle

    my_rectangle_1 = Rectangle(8, 4)
    print(my_rectangle_1)
    print("--")
    my_rectangle_1.print_symbol = "&"
    print(my_rectangle_1)
    print("--")

    my_rectangle_2 = Rectangle(2, 1)
    print(my_rectangle_2)
    print("--")
    Rectangle.print_symbol = "C"
    print(my_rectangle_2)
    print("--")

    my_rectangle_3 = Rectangle(7, 3)
    print(my_rectangle_3)

    print("--")

    my_rectangle_3.print_symbol = ["C", "is", "fun!"]
    print(my_rectangle_3)

    print("--")

    user@ubuntu:~/$ ./7-main.py
    ########
    ########
    ########
    ########
    --
    &&&&&&&&
    &&&&&&&&
    &&&&&&&&
    &&&&&&&&
    --
    ##
    --
    CC
    --
    CCCCCCC
    CCCCCCC
    CCCCCCC
    --
    ['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
    ['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
    ['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
    --
    Bye rectangle...
    Bye rectangle...
    Bye rectangle...
    user@ubuntu:~/$ 
    ```

### 8. 🟦 Compare Rectangles
Write a class Rectangle that defines a rectangle by: (based on `7-rectangle.py`)

- **File:** `8-rectangle.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 8-main.py
    #!/usr/bin/python3
    Rectangle = __import__('8-rectangle').Rectangle

    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)

    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")


    my_rectangle_2.width = 10
    my_rectangle_2.height = 5
    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")

    user@ubuntu:~/$ ./8-main.py
    my_rectangle_1 is bigger or equal to my_rectangle_2
    my_rectangle_2 is bigger than my_rectangle_1
    Bye rectangle...
    Bye rectangle...
    user@ubuntu:~/$ 
    ```

### 9. 🟦 A Square is a Rectangle
Write a class Rectangle that defines a rectangle by: (based on `8-rectangle.py`)

- **File:** `9-rectangle.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 9-main.py
    #!/usr/bin/python3
    Rectangle = __import__('9-rectangle').Rectangle

    my_square = Rectangle.square(5)
    print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
    print(my_square)

    user@ubuntu:~/$ ./9-main.py
    Area: 25 - Perimeter: 20
    #####
    #####
    #####
    #####
    #####
    Bye rectangle...
    user@ubuntu:~/$ 
    ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-more_classes`
