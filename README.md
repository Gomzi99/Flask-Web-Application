# Flask Web App 

Here i was only able to do uptil the first part out of the three required as was facing errors and issues.

## Setup & Installation

Make sure you have the latest version of Python and MySQL installed. 

```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```

## Setting Up MySQL Database:

1. Create a MySQL database named db_name.
   
    ```sql
    CREATE DATABASE IF NOT EXISTS db_name;
    ```

2.  Use the Database

    ```sql
    USE db_name;
    ```

3. Run the following SQL script to set up the required tables:

    ```sql
    -- database_setup.sql
    CREATE TABLE user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(20) UNIQUE NOT NULL,
        password VARCHAR(60) NOT NULL
    );

    CREATE TABLE inventory_item (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        quantity INT NOT NULL
    );
    ```

## Running The App

```bash
python main.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`
