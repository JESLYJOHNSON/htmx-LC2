import csv

from django.db import models


# ManufacturerName,idManufacturer,WinItemName,WiseItemNumber,ProductNumber,ItemNumber,ItemStatus,SimilarityScore,ComodityNumber
class win(models.Model):
                ItemNumber =  models.CharField(max_length=100)
                ProductNumber = models.CharField(max_length=100)
                WiseItemNumber =   models.CharField(max_length=100)
                ManufacturerName = models.CharField(max_length=500)
                idManufacturer = models.CharField(max_length=100)
                WinItemName = models.CharField(max_length=500)
                SimilarityScore = models.CharField(max_length=500)
                ItemStatus =   models.CharField(max_length=100) 
                MainframeDescription = models.CharField(max_length=100)
                ComodityNumber=models.TextField()
                CatalogNnumber=models.TextField()
                UPC=models.TextField()
                VENDOR_ITEM_NUMBER=models.TextField()
                VENDOR_NUMBER =models.TextField()



                # CategoryKey = models.CharField(max_length=100)

                # PIK = models.CharField(max_length=100)
                # ItemLCP = models.CharField(max_length=100)
                # CatalogNnumber = models.CharField(max_length=100)
                # OrderNumber = models.CharField(max_length=100)
                # Brand =  models.CharField(max_length=100)

                # idManufacturer = models.CharField(max_length=100)
                
# You can run this function in the django shell after creating the database

def load_data():
    instances = []
    required_fields = [
        "ItemNumber", 
        "ProductNumber", 
        "WiseItemNumber",
        "ManufacturerName",
        "MainframeDescription",
        "WinItemName", 
        "SimilarityScore", 
        "ItemStatus",
        "idManufacturer",
        "ComodityNumber",
        "CatalogNnumber",
        "UPC",
        "VENDOR_ITEM_NUMBER",
        "VENDOR_NUMBER",

    ]

    with open("./Victory.csv", mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print("CSV Fieldnames (headers found):", reader.fieldnames)
        

        for row in reader:
            instances.append(win(
                ItemNumber=row.get("ItemNumber", "").strip(),
                ProductNumber=row.get("ProductNumber", "").strip(),
                idManufacturer=row.get("idManufacturer", "").strip(),
                WiseItemNumber=row.get("WiseItemNumber", "").strip(),
                MainframeDescription=row.get("MainframeDescription", "").strip(),
                ManufacturerName=row.get("ManufacturerName", "").strip(),
                WinItemName=row.get("WinItemName", "").strip(),
                SimilarityScore=row.get("SimilarityScore", "").strip(),
                ItemStatus=row.get("ItemStatus", "").strip(),
                ComodityNumber=row.get("ComodityNumber", "").strip(),
                CatalogNnumber=row.get("CatalogNnumber", "").strip(),
                UPC=row.get("UPC", "").strip(),
                VENDOR_ITEM_NUMBER=row.get("VENDOR_ITEM_NUMBER", "").strip(),
                VENDOR_NUMBER=row.get("VENDOR_NUMBER", "").strip(),
            ))

    win.objects.bulk_create(instances)
    print(f" Imported {len(instances)} records.")

        # for row in reader:
        #     if not all(field in row for field in required_fields):
        #         print("Skipping row due to missing fields:", row)
        #         continue

        # win.objects.create(
        #         ItemNumber=row["ItemNumber"],
        #         ProductNumber=row["ProductNumber"],
        #         WiseItemNumber=row["WiseItemNumber"],
        #         ManufacturerName=row["ManufacturerName"],
        #         WinItemName=row["WinItemName"],
        #         SimilarityScore=row["SimilarityScore"],
        #         ItemStatus=row["ItemStatus"]
        #     )



# def load_data():
#     required_fields = [
#         "ItemNumber", 
#         # "CategoryKey",
#          "ProductNumber", 
#          "WiseItemNumber",
#         #    "PIK",
#         # "ItemLCP", 
#         # "CatalogNnumber",
#         #   "OrderNumber",
#             # "Brand", 
#             "ManufacturerName",
#         "WinItemName", "SimilarityScore", 
#         # "idManufacturer", 
#         "ItemStatus"
#     ]

#     with open("data.csv", mode='r', encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         print("CSV Fieldnames (headers found):", reader.fieldnames)

#         for row in reader:
#             # Skip rows missing any required fields
#             if not all(field in row for field in required_fields):
#                 print("Skipping row due to missing fields:", row)
#                 continue

#             win.objects.create(
#                 ItemNumber=row["ItemNumber"],
#                 CategoryKey=row["CategoryKey"],
#                 ProductNumber=row["ProductNumber"],
#                 WiseItemNumber=row["WiseItemNumber"],
#                 PIK=row["PIK"],
#                 ItemLCP=row["ItemLCP"],
#                 CatalogNnumber=row["CatalogNnumber"],
#                 OrderNumber=row["OrderNumber"],
#                 Brand=row["Brand"],
#                 ManufacturerName=row["ManufacturerName"],
#                 WinItemName=row["WinItemName"],
#                 SimilarityScore=row["SimilarityScore"],
#                 idManufacturer=row["idManufacturer"],
#                 ItemStatus=row["ItemStatus"]
#             )
# def load_data():
#     # You can download the CSV from the following link.
#     # https://github.com/HipsterVizNinja/random-data/tree/main/Music/hot-100
#     win_data = []
#     try:
#         with open("data.csv", mode='r', encoding='utf-8') as f:
#             reader = csv.DictReader(f)
#             print("CSV Fieldnames (headers found):", reader.fieldnames)

#             for i, row in enumerate(reader):
#                 # Optionally, strip whitespace from all string values if needed
#                 # For this request, we'll keep it simple and just append the row as is.
#                 # If you need cleaned data later, you can add a loop here:
#                 # cleaned_row = {key.strip(): value.strip() for key, value in row.items()}
#                 # all_rows.append(cleaned_row)

#                 win_data.append(row) # Add the dictionary representation of the row to our list

#     except FileNotFoundError:
#         print("Error: data.csv not found. Please ensure the file is in the same directory as the script.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

#     print(f"Successfully loaded {len(win_data)} rows from data.csv.")
                
        # print(reader.fieldnames)
        # for row in reader:
        #     if (row["WinItemName"], row["ItemNumber"],row["SimilarityScore"] ) not in win_data:
        #         win_data[(row["WinItemName"], row["ItemNumber"],row["SimilarityScore"])] = {
        #             "ItemStatus": row["ItemStatus"],
        #             "ProductNumber": row["ProductNumber"],
        #             "WiseItemNumber": row["WiseItemNumber"],
        #             "ManufacturerName": row["ManufacturerName"],
                    
        #         }

        #           # If the item_key already exists, it means we found a "matching" row.
        #             # As requested to "display the details that closely matches",
        #             # we will update the existing entry with the details from the current row.
        #             # This means the last row encountered for a given key will "win".
        #     else:
        #         item_key = (row["WinItemName"], row["ItemNumber"], row["SimilarityScore"])
        #         print(f"Duplicate item_key found (row {i+2}): {item_key}. Overwriting details.") # i+2 for 0-indexed row + header
        #         win_data[item_key] = {
        #                 "ItemStatus": row["ItemStatus"],
        #                 "ProductNumber": row["ProductNumber"],
        #                 "WiseItemNumber": row["WiseItemNumber"],
        #                 "ManufacturerName": row["ManufacturerName"],
        #             }
    # except FileNotFoundError:
    #     print("Error: data.csv not found. Please ensure the file is in the same directory as the script.")
    # except KeyError as e:
    #     print(f"Error: Missing expected column in CSV: {e}. Check your CSV header and ensure it matches the code.")
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e}")

                    
    
                
    # for s in win_data:
    #     win.objects.create(
    #         ItemNumber= s[0],  
    #         ProductNumber = s[1],
    #         WiseItemNumber = s[2],
    #         ManufacturerName =win_data[s]["ManufacturerName"],
    #         WinName = win_data[s]['WinName'],
    #         SimilarityScore =win_data[s]["SimilarityScore"],
    #         ItemStatus =win_data[s]["ItemStatus"] 
    #     )


# from app.models import win  # Adjust import if needed


