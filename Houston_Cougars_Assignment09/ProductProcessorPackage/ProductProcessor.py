# File Name : ProductProcessor.py
# Student Name: Ryan Jacob
# email:  Jacobry@mail.uc.edu
# Assignment Number: Assignment 09
# due date: 04/03/2025
# Course #/Section:  IS4010-002
# Brief Description of the assignment:  The assignment requires developing a program that connects to a SQL Server, 
# retrieves product data from the Grocery Store Simulator database, randomly selects a product, and looks up its manufacturer information.
# the product_data module retrieves product and manufacturer data, 
# and implements functionality to randomly select a product and fetch its associated manufacturer name.   
    
import random

class ProductProcessor:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

    def fetchAllProducts(self):
        self.cursor.execute("SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct")
        return self.cursor.fetchall()

    def getRandomProductInfo(self, products):
        chosen = random.choice(products)
        product_id = chosen.ProductID
        description = chosen.Description
        manufacturer_id = chosen.ManufacturerID
        brand_id = chosen.BrandID
        return {
            "ProductID": product_id,
            "Description": description,
            "ManufacturerID": manufacturer_id,
            "BrandID": brand_id
        }

    def getManufacturerName(self, manufacturer_id):
        self.cursor.execute("SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = ?", manufacturer_id)
        result = self.cursor.fetchone()
        return result.Manufacturer if result else None