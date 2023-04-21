# for working with DB 
import sqlite3
# time
import datetime
# for easily work with dicts
import json
# settings for DB
from services.settings.database_base import TABLE_USERS, CREATE_TABLES
# for easily typing tuples
from typing import NamedTuple


class User(NamedTuple):
    login      : str
    password   : str
    os_version : str


# for working with DB
class DB:
    def __init__(self) -> None:
        global CREATE_TABLES
        self.basename = 'sqlite.db'
        self.connection = sqlite3.connect(self.basename)
        self.cursor = self.connection.cursor()
        if CREATE_TABLES:
            self.create_all_tables(
                TABLE_USERS
            )
            CREATE_TABLES = False
    def execute(
        self, 
        query: str, 
        is_commit: int = 0
    ) -> object:
        try:
            result = self.cursor.execute(query)
            if is_commit == 1:
                self.connection.commit()
                return 0
            else:
                return result.fetchall()
        except Exception as e:
            print(f" --- Exception: <{e}> ---")
            return 1

    def create_all_tables(self, *tables: list[str]) -> None:
        for table in tables:
            self.execute(query=table, is_commit=1)
            
    def registrate_user(self, data: User) -> int:
        user_exists = self.execute(
            query=f'''
                SELECT id FROM users
                WHERE login='{data.login}'
                AND 
                password='{data.password}'
            '''
        )

        if len(user_exists) > 0:
            return 1

        result = self.execute(
            query=f'''
                INSERT INTO users (login, password, os_version)
                VALUES ('{data.login}', '{data.password}', '{data.os_version}')
            ''',
            is_commit=1
        )

        return result

    def get_all_users(self) -> list:
        result = self.execute(
            query='''
                SELECT * FROM users
            '''
        ) 

        return result
