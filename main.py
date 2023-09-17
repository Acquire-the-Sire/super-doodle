import mysql.connector
from mysql.connector import Error

# these files are imported from the lecture material
import credentials
import sqlfunc

myCreds = credentials.Creds()
conn = sqlfunc.create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)