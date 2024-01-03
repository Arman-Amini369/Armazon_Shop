from django.db import models
from accounts.models import CustomerAccount
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200 ,null=False ,blank=False)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category ,on_delete=models.CASCADE)
    price = models.IntegerField(null=False ,blank=False)
    image = models.ImageField(null=True ,blank=True)
    description = models.TextField(max_length=200)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantities = models.PositiveSmallIntegerField()

class Comment(models.Model):
    user = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    body = models.TextField()
    SCORE = (
          ("0%", "0%"),
          ("10%", "10%"),
          ("20%", "20%"),
          ("30%", "30%"),
          ("40%", "40%"),
          ("50%", "50%"),
          ("60%", "60%"),
          ("70%", "70%"),
          ("80%", "80%"),
          ("90%", "90%"),
          ("100%", "100%"),
	)
    score = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return f'{self.user} - {self.body[:30]} - {self.product}'