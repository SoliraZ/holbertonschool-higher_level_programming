# 🐍 Python Serialization

This repository contains various Python scripts that demonstrate different serialization techniques including JSON, Pickle, CSV, and XML.

## 📋 Tasks

### 0. 📄 Basic Serialization
In this task, we create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

- **File:** `task_00_basic_serialization.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat main_00_basic_serialization.py 
    #!/usr/bin/env python3
    from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')

    # Output: The data has been serialized and saved to 'data.json'
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')

    # Output: The deserialized data
    print("Deserialized Data:")
    print(deserialized_data)

    user@ubuntu:~/$ ./main_00_basic_serialization.py 
    Data serialized and saved to 'data.json'.
    Deserialized Data:
    {'name': 'John Doe', 'age': 30, 'city': 'New York'}
    ```

### 1. 🥒 Pickling Custom Classes
We learn how to serialize and deserialize custom Python objects using the pickle module.

- **File:** `task_01_pickle.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat main_01_pickle.py 
    #!/usr/bin/env python3
    from task_01_pickle import CustomObject

    # Create an instance of CustomObject
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize the object
    obj.serialize("object.pkl")

    # Deserialize the object into a new instance
    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    new_obj.display()

    user@ubuntu:~/$ ./main_01_pickle.py 
    Original Object:
    Name: John
    Age: 25
    Is Student: True

    Deserialized Object:
    Name: John
    Age: 25
    Is Student: True
    ```

### 2. 📊 Converting CSV Data to JSON Format
We gain experience in reading data from one format (CSV) and converting it into another format (JSON) using serialization techniques.

- **File:** `task_02_csv.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat main_02_csv.py 
    #!/usr/bin/env python3
    from task_02_csv import convert_csv_to_json

    csv_file = "data.csv"
    convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")

    user@ubuntu:~/$ ./main_02_csv.py 
    Data from data.csv has been converted to data.json
    ```

### 3. 📜 Serializing and Deserializing with XML
We explore serialization and deserialization using XML as an alternative format to JSON.

- **File:** `task_03_xml.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat main_03_xml.py 
    #!/usr/bin/env python3
    from task_03_xml import serialize_to_xml, deserialize_from_xml

    def main():
        sample_dict = {
            'name': 'John',
            'age': '28',
            'city': 'New York'
        }

        xml_file = "data.xml"
        serialize_to_xml(sample_dict, xml_file)
        print(f"Dictionary serialized to {xml_file}")

        deserialized_data = deserialize_from_xml(xml_file)
        print("\nDeserialized Data:")
        print(deserialized_data)

    if __name__ == "__main__":
        main()

    user@ubuntu:~/$ ./main_03_xml.py 
    Dictionary serialized to data.xml

    Deserialized Data:
    {'name': 'John', 'age': '28', 'city': 'New York'}
    ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-serialization`