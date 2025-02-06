# 🟦 Python ABC

This repository contains various Python scripts that demonstrate advanced programming concepts related to Abstract Base Classes (ABCs) and other object-oriented programming techniques.

## 📋 Tasks

### 0. 🟦 Abstract Animal Class and its Subclasses
In this task, we create an abstract class named `Animal` using the ABC package. This class has an abstract method called `sound`. We then create two subclasses of `Animal`: `Dog` and `Cat`, implementing the `sound` method to return "Bark" and "Meow" respectively.

- **File:** `task_00_abc.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat main_00_abc.py 
    #!/usr/bin/env python3
    from task_00_abc import Animal, Dog, Cat

    bobby = Dog()
    garfield = Cat()

    print(bobby.sound())
    print(garfield.sound())

    animal = Animal()
    print(animal.sound())

    user@ubuntu:~/$ ./main_00_abc.py 
    Bark
    Meow
    Traceback (most recent call last):
      File "main_00_abc.py", line 10, in <module>
        animal = Animal()
    TypeError: Can't instantiate abstract class Animal with abstract method sound
    ```

### 1. 🟦 Shapes, Interfaces, and Duck Typing
We design an abstract class named `Shape` with two abstract methods: `area` and `perimeter`. We implement two concrete classes: `Circle` and `Rectangle`, both inheriting from `Shape`. We also write a function `shape_info` that prints the area and perimeter of a shape.

- **File:** `task_01_duck_typing.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat main_01_duck_typing.py 
    #!/usr/bin/env python3
    from task_01_duck_typing import Circle, Rectangle, shape_info

    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)

    user@ubuntu:~/$ ./main_01_duck_typing.py 
    Area: 78.53981633974483
    Perimeter: 31.41592653589793
    Area: 28
    Perimeter: 22
    ```

### 2. 🟦 Extending the Python List with Notifications
We create a class named `VerboseList` that extends the Python list class. This custom class prints a notification message every time an item is added or removed using the `append`, `extend`, `remove`, or `pop` methods.

- **File:** `task_02_verboselist.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat main_02_verboselist.py 
    #!/usr/bin/env python3
    from task_02_verboselist import VerboseList

    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)

    user@ubuntu:~/$ ./main_02_verboselist.py 
    Added [4] to the list.
    Extended the list with [2] items.
    Removed [2] from the list.
    Popped [6] from the list.
    Popped [1] from the list.
    ```

### 3. 🟦 CountedIterator - Keeping Track of Iteration
We create a class named `CountedIterator` that extends the built-in iterator obtained from the `iter` function. The `CountedIterator` keeps track of the number of items that have been iterated over by overriding the `__next__` method.

- **File:** `task_03_countediterator.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat main_03_countediterator.py 
    #!/usr/bin/env python3
    from task_03_countediterator import CountedIterator

    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")

    user@ubuntu:~/$ ./main_03_countediterator.py 
    Got 1, total 1 items iterated.
    Got 2, total 2 items iterated.
    Got 3, total 3 items iterated.
    Got 4, total 4 items iterated.
    No more items.
    ```

### 4. 🟦 The Enigmatic FlyingFish - Exploring Multiple Inheritance
We construct a `FlyingFish` class that inherits from both a `Fish` class and a `Bird` class. Within `FlyingFish`, we override methods from both parents to understand multiple inheritance and method resolution order.

- **File:** `task_04_flyingfish.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat main_04_flyingfish.py 
    #!/usr/bin/env python3
    from task_04_flyingfish import Fish, FlyingFish

    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    user@ubuntu:~/$ ./main_04_flyingfish.py 
    The flying fish is swimming!
    The flying fish is soaring!
    The flying fish lives both in water and the sky!
    ```

### 5. 🟦 The Mystical Dragon - Mastering Mixins
We design two mixin classes, `SwimMixin` and `FlyMixin`, each equipped with methods `swim` and `fly` respectively. We then construct a class `Dragon` that inherits from both these mixins, demonstrating that a `Dragon` instance can both swim and fly.

- **File:** `task_05_dragon.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat main_05_dragon.py 
    #!/usr/bin/env python3
    from task_05_dragon import Dragon

    dragon = Dragon()
    dragon.swim()  # Outputs: The creature swims!
    dragon.fly()   # Outputs: The creature flies!
    dragon.roar()  # Outputs: The dragon roars!

    user@ubuntu:~/$ ./main_05_dragon.py 
    The creature swims!
    The creature flies!
    The dragon roars!
    ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-abc`