# app/models.py

import csv
from django.db import models

class win(models.Model):
    # --- Your Model Fields ---
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

    # --- New Class Method for Loading Data ---
    @classmethod
    def load_data(cls):
        """
        More efficient and automatic data loader.
        This is now a class method of the 'win' model.
        """
        # Get all field names directly from the model itself.
        model_fields = [field.name for field in cls._meta.get_fields() if not field.is_relation]
        
        instances_to_create = []
        
        # Update the path to your CSV file if it's different.
        with open("./Victory.csv", mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                model_data = {}
                # Automatically map all columns that exist in both the model and the CSV.
                for field_name in model_fields:
                    if field_name in row and row[field_name] is not None:
                        model_data[field_name] = row[field_name].strip()
                
                if model_data:
                    instances_to_create.append(cls(**model_data))

        # Use bulk_create for high-performance import.
        cls.objects.all().delete()
        cls.objects.bulk_create(instances_to_create, batch_size=500)
        
        print(f"Imported {len(instances_to_create)} records.")