import ibm_db
import os


def get_connection():
    dsn = (
        "DATABASE={};"
        "HOSTNAME={};"
        "PORT={};"
        "PROTOCOL={};"
        "UID={};"
        "PWD={};").format(os.getenv("DATABASE"), os.getenv("HOSTNAME"), os.getenv("DB2_PORT"), os.getenv("PROTOCOL"), os.getenv("UID"), os.getenv("PWD"))
    try:
        conn = ibm_db.connect(dsn, "", "")
        return conn
    except:
        print("Unable to connect")

    return None


def create_schema(connection):
    table_creation = ibm_db.exec_immediate(
        connection, "CREATE TABLE students(st_id VARCHAR(20),st_name VARCHAR(20),st_stream VARCHAR(20))")
    ibm_db.close(connection)


def insert_data_with_connection(connection, query, **kwargs):

    stmt = ibm_db.prepare(connection, query)
    for index, (key, value) in enumerate(kwargs.items()):
        ibm_db.bind_param(stmt, index+1, value)
    ibm_db.execute(stmt)
    ibm_db.close(connection)


if __name__ == "__main__":
    connection = get_connection()
    if(connection is not None):
        create_schema(connection)
        insert_data_with_connection(connection, "INSERT INTO students (st_id,st_name,st_stream) VALUES(?,?,?);", sti='2',
                                    stn='Shravankumar',
                                    sts='Mechanical')
