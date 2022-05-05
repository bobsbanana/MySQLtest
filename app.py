import mysql.connector
from database import _Datatools


db = mysql.connector.connect(
host="127.0.0.1",
port="3306",
user="root",
password="qigjeh-tajpuv-2xopPu?",
database="users"
)


app = _Datatools(db)
app.addUser("userInfo","jill","3^%^")
db.commit()
app.displayDatabase()