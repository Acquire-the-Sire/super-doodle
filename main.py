import mysql.connector
from mysql.connector import Error

# these files are imported from the lecture material
import credentials
import sqlfunc

myCreds = credentials.Creds()
conn = sqlfunc.create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
create_sales_table = """CREATE TABLE IF NOT EXISTS sales(
    id INT,
    seller VARCHAR(255) NOT NULL,
    product VARCHAR(255) NOT NULL,
    quantity INT,
    price FLOAT,
    PRIMARY KEY(id)
)"""
sqlfunc.execute_query(conn, create_sales_table)
# populate_sales_table = """
# INSERT INTO sales (id, seller, product, quantity, price) VALUES
# (1, "James", "Tissues", 50, 1.99),
# (2, "John", "Drill", 3, 59.99),
# (3, "Jack", "Fertilizer", 10, 33.50),
# (4, "James", "NyQuil", 3, 7.99),
# (5, "John", "Wheelbarrow", 3, 45.39),
# (6, "Jack", "PVC Pipe 24cm", 100, 5.99),
# (7, "James", "Chicken Soup", 3, 4.99),
# (8, "John", "Gloves", 6, 15.99),
# (9, "Jack", "Twine", 20, 7.50)
# """
# sqlfunc.execute_query(conn, populate_sales_table)
data_retrieval = """SELECT * FROM sales"""
data = sqlfunc.execute_read_query(conn, data_retrieval)
seller_list = []
for i in data:
    if i['seller'] not in seller_list:
        seller_list.append(i['seller'])
print("Available Sellers:")
for i in seller_list:
    print(i)
seller_search = input("Enter the name of the seller:\n")
seller_search = seller_search.casefold()
seller_search = seller_search.capitalize()
if seller_search not in seller_list:
    print("This seller is unavailable.")
else:
    print("Sales report for " + seller_search + ":")
    seller_total = 0
    for i in data:
        if i['seller'] == seller_search:
            print("Product: " + i['product'] + ", Quantity: " + i['quantity'] + ", Price: $" + i['price'] + ", Total: $"
                  + i['quantity'] * i['product'])
            seller_total += i['quantity'] * i['product']
    print("Total sales for " + seller_search + ": $" + seller_total)