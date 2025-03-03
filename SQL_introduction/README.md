# 📊 SQL Introduction

This directory contains various SQL scripts for managing and interacting with MySQL databases.

## 📋 Tasks

### 0. 📂 List Databases
Lists all databases of your MySQL server.

- **File:** `0-list_databases.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    Database
    information_schema
    mysql
    performance_schema
    sys
    user@ubuntu:~/$
    ```

### 1. 🗄️ Create Database
Creates the database `hbtn_0c_0` if it doesn't already exist.

- **File:** `1-create_database_if_missing.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    user@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    Database
    information_schema
    hbtn_0c_0
    mysql
    performance_schema
    user@ubuntu:~/$ 
    ```

### 2. 🗑️ Remove Database
Deletes the database `hbtn_0c_0` if it exists.

- **File:** `2-remove_database.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    user@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    Database
    information_schema
    mysql
    performance_schema
    sys        
    user@ubuntu:~/$ 
    ```

### 3. 📋 List Tables
Lists all the tables of a specified database.

- **File:** `3-list_tables.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
    Enter password: 
    Tables_in_mysql
    columns_priv
    component
    db
    default_roles
    engine_cost
    func
    general_log
    global_grants
    gtid_executed
    help_category
    help_keyword
    help_relation
    help_topic
    innodb_index_stats
    innodb_table_stats
    password_history
    plugin
    procs_priv
    proxies_priv
    replication_asynchronous_connection_failover
    replication_asynchronous_connection_failover_managed
    role_edges
    server_cost
    servers
    slave_master_info
    slave_relay_log_info
    slave_worker_info
    slow_log
    tables_priv
    time_zone
    time_zone_leap_second
    time_zone_name
    time_zone_transition
    time_zone_transition_type
    user
    user@ubuntu:~/$ 
    ```

### 4. 📝 Create First Table
Creates a table called `first_table` in the current database.

- **File:** `4-first_table.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    user@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    Tables_in_hbtn_0c_0
    first_table
    user@ubuntu:~/$ 
    ```

### 5. 📜 Full Table Description
Prints the description of the table `first_table` from the database `hbtn_0c_0`.

- **File:** `5-full_table.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    Table   Create Table
    first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci        
    user@ubuntu:~/$ 
    ```

### 6. 📄 List All Rows
Lists all rows of the table `first_table` from the database `hbtn_0c_0`.

- **File:** `6-list_values.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    user@ubuntu:~/$ 
    ```

### 7. ➕ Insert Row
Inserts a new row into the table `first_table` with `id = 89` and `name = 'Best School'`.

- **File:** `7-insert_value.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    user@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    id  name
    89  Best School
    user@ubuntu:~/$ 
    ```

### 8. 🔢 Count Records
Displays the number of records with `id = 89` in the table `first_table`.

- **File:** `8-count_89.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
    Enter password: 
    3
    user@ubuntu:~/$ 
    ```

### 9. 🏗️ Full Table Creation
Creates a table `second_table` and adds multiple rows.

- **File:** `9-full_creation.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    user@ubuntu:~/$ 
    ```

### 10. 🏆 List by Best Score
Lists all records of the table `second_table` ordered by score (top first).

- **File:** `10-top_score.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    score   name
    14  Bob
    10  John
    8   George
    3   Alex
    user@ubuntu:~/$ 
    ```

### 11. 🎯 Select Best Scores
Lists all records with a score >= 10 in the table `second_table`.

- **File:** `11-best_score.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    score   name
    14  Bob
    10  John
    user@ubuntu:~/$ 
    ```

### 12. 🚫 No Cheating
Updates the score of `Bob` to 10 in the table `second_table`.

- **File:** `12-no_cheating.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    user@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    score   name
    10  John
    10  Bob
    8   George
    3   Alex
    user@ubuntu:~/$ 
    ```

### 13. 🧹 Remove Low Scores
Removes all records with a score <= 5 in the table `second_table`.

- **File:** `13-change_class.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    user@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    score   name
    10  John
    10  Bob
    8   George
    user@ubuntu:~/$ 
    ```

### 14. 📊 Compute Average
Computes the score average of all records in the table `second_table`.

- **File:** `14-average.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    average
    9.3333
    user@ubuntu:~/$ 
    ```

### 15. 📈 Number by Score
Lists the number of records with the same score in the table `second_table`.

- **File:** `15-groups.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    score   number
    10  2
    8   1
    user@ubuntu:~/$ 
    ```

### 16. 🗃️ List Non-Empty Names
Lists all records of the table `second_table` without rows that have no name value.

- **File:** `16-no_link.sql`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    score   name
    18  Aria
    12  Aria
    10  John
    10  Bob
    user@ubuntu:~/$ 
    ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `SQL_introduction`