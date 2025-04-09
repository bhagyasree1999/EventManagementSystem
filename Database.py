import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="141.209.241.57",
        user="tiruv1h",
        password="mypass",
        database="BIS698W1830_GRP1"
    )