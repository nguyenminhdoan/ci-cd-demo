import mysql.connector
import unittest
import os


class TestMySQLConnection(unittest.TestCase):
    def test_connection(self):
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "127.0.0.1"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", ""),
            database=os.getenv("MYSQL_DATABASE", "test_db")
        )

        self.assertTrue(connection.is_connected())
        connection.close()


if __name__ == '__main__':
    unittest.main()
