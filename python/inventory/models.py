from django.db import models


class Equipmentcategory(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(unique=True,max_length=45)
    date_created=models.DateField(auto_now=True)
    class Meta:
        vebrose_name_plural="Equipment Categories"
    def __str__(self) :
       return self,category_name


class Products(models.Model):
    product_id=models.AutoField(primary_key=True)
    category_id=models.models.ForeignKey(EquipmentCategory,on_delete=models.CASCADE)
    product_name=models.CharField(unique=True,max_length=45)
    unit_price=models,models.IntegerField(default=0)
    sales_price=models=models.IntegerField(default=0)
    available_stock=models.models.IntegerField(default=0)
    unit_measure=models.models.CharField(max_length=10)
    date_updated=models.models.DateField(auto_now=True)
    class Meta:
        vebrose_name_plural="products"
    def __str__(self):
       return self.product_name


       class Transactions(models.Model):
        transaction_id=models.AutoField(primary_key=True)
        Product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
        transaction_type=models.CharField(max_length=0)
        stock_taken=models.IntegerField(default=0)
        transaction_amount=models.IntegerField(default=0)
        transaction_date=models.DateField(auto_now=True)
        class Meta:
            verbose_name_plural="Transactions"
        def __str__(self):
            return self.Transaction
            
