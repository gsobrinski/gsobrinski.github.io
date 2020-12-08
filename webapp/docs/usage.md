# Web App Organization & Usage

## Organization
- app.py
    - main program - run using python3 app.py
    - serves up pages and retrieves form data

- /static - contains any CSS & JS files
- /templates - contains html files
- /database - contains all database code (sql and python)

    - /models/info_model.py

        - initalize classes for database table objects
        - login_info is the object for the logins db table
        - config_info is the object for the config db table
    - /sql/create_tables.sql
        - runs on startup to initialize tables if they don't exist yet
    - /sql/add_config.sql
        - runs on startup to initialize config values in settings if they don't exist yet
    - /sql/add_login.sql 
        - just for testing
    - __init__.py
        - initializes the databases

    - dbconn.py
        - add_login inserts into the logins db
        - add_config updates the config db
        - get_config retrieves the config db information for the index page

## Usage
### raspberry pi server: 69.253.212.184:5000