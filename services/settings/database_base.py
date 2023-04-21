CREATE_TABLES = True


# table of user
# id - int 
# login - str 32
# password - str 32
# version of os - str 64
TABLE_USERS = '''

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(32) NOT NULL,
    password VARCHAR(32) NOT NULL,
    os_version VARCHAR(64) NOT NULL
)

'''
