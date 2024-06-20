from apscheduler.schedulers.background import BackgroundScheduler
from .models import *
import pandas as pd

def StartProductScheduler():
    scheduler = BackgroundScheduler()
    scheduler.remove_all_jobs()
    scheduler.add_job(ProductJob, 'interval', seconds=2)
    scheduler.start()

def ProductJob():

    products = ProductFiles.objects.filter(fileRead=False)
    for product in products:
        file = pd.read_excel(product.file.path)
        for index, row in file.iterrows():
            if row['Name'] is not None and row['categoryFK'] is not None and row['weight'] is not None and row['description'] is not None and row['barCode'] is not None and row['image'] is not None:
                productcategory = ProductCategory.objects.get(name=row['categoryFK'])
                Product.objects.create(
                    name=row['Name'],
                    categoryFK=productcategory,
                    weight=row['weight'],
                    description=row['description'],
                    barCode=row['barCode'],
                    image=row['image']
                )
        product.fileRead = True
        product.save()


