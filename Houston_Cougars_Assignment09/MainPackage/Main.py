#Main.py
# Luke Elmore, Ryan Jacob



import random
from DatabaseManagementPackage.DataBaseManagement import *
from ProductProcessorPackage.ProductProcessor import*

if __name__ == "__main__":

    db_manager = DatabaseManagement()
    conn = db_manager.connectToDatabase()



    processor = ProductProcessor(conn)
    products = processor.fetchAllProducts()

    # Pick a random product
    product_info = processor.getRandomProductInfo(products)

    # Get the manufacturer name
    manufacturer_name = processor.getManufacturerName(product_info["ManufacturerID"])

    #Get the brand name
    brand_name = processor.getBrandName(product_info["BrandID"])

    ItemsSold = processor.getItemsSold(product_info["ProductID"])


    # Output results
    print(f"Random Product: {product_info['Description']}")
    print(f"ProductID: {product_info['ProductID']}")
    print(f"ManufacturerID: {product_info['ManufacturerID']}")
    print(f"BrandID: {product_info['BrandID']}")
    print(f"Manufacturer Name: {manufacturer_name}")

    sentence = f"The product '{product_info['Description']}' from {manufacturer_name} under the brand '{brand_name}' has sold {ItemsSold} units."
    print(sentence)


    #Look at the tables and columns
    #cursor = conn.cursor()
    #cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")

# Fetch all tables
#tables = cursor.fetchall()

# For each table, fetch the column headers
#for table in tables:
    #table_name = table.TABLE_NAME
    #print(f"Columns in {table_name}:")
    
    # Query to get the columns for each table
    #cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = ?", table_name)
    
    # Fetch and print column headers
    #columns = cursor.fetchall()
    #for column in columns:
       # print(f"  {column.COLUMN_NAME}")
