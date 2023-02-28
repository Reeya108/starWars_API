import pymysql

"""
github.com"""


def make_connection():
    try:
        connection = pymysql.connect(
            user="root",
            password="ranaderiya@123",
            host="127.0.0.1",
            port=3306,
            database="starwarsDB"
        )
    except pymysql.err.Error as ex:
        print(f"[ ERROR ] cannot establish connection - {ex}")

    return connection


if __name__ == "__main__":
    conn = make_connection()
    breakpoint()