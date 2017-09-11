import pymysql
import dbconfig


class DBHelper:
    @staticmethod
    def connect(database="crimemap"):
        return pymysql.connect(host='localhost',
                               user=dbconfig.db_user,
                               passwd=dbconfig.db_password,
                               db=database)

    def find_all(self):
        """Fetch all descriptions """
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        finally:
            connection.close()

    def add(self, data):
        """Add a new crime"""
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (description) VALUES (%s);"
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
        finally:
            connection.close()

    def clear_all(self):
        """Clear all the inserted data"""
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
