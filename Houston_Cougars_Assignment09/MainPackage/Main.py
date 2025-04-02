#Main.py
# Luke Elmore, Ryan Jacob

import random
from DatabaseManagementPackage.DataBaseManagement import *
from ProductProcessorPackage.ProductProcessor import*


db_manager = DatabaseManagement()
conn = db_manager.connectToDatabase()



processor = ProductProcessor(conn)
products = processor.fetchAllProducts()

# Pick a random product
product_info = processor.getRandomProductInfo(products)

# Get the manufacturer name
manufacturer_name = processor.getManufacturerName(product_info["ManufacturerID"])

# Output results
print(f"Random Product: {product_info['Description']}")
print(f"ProductID: {product_info['ProductID']}")
print(f"ManufacturerID: {product_info['ManufacturerID']}")
print(f"BrandID: {product_info['BrandID']}")
print(f"Manufacturer Name: {manufacturer_name}")

