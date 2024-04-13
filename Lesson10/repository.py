import sqlite3
class Repository:
    def __init__(self, database: str, timeout: float):
        self.DataBase: str = database
        self.TimeOut: float = timeout
    def Query(self, sQuery: str):
        try:
            connection = sqlite3.connect(self.DataBase, self.TimeOut)
            cursor = connection.cursor()
            cursor.execute(sQuery)
            connection.commit()
        except:
            raise
        finally:
            connection.close()