import mysql.connector
connect_args = {
    "port": 3306,
    "user": "root",
    "password": "thienulti1997",
    };
#----------connect() function ------
db1= mysql.connector.connect(
    **connect_args
    )
print (
    "MySQL connection ID for db1: {0}"
    .format(db1.connection_id)
    )
db1.close()
