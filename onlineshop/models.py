from django.db import models

# Create your models here.
# The `TimestampsModel` class is an abstract model in Python that includes fields for creation and
# update timestamps.
class TimestampsModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class category(TimestampsModel):
    category_name=models.CharField(max_length=100)
    description=models.TextField(max_length=250)

    def __str__(self):
        """
        The above function defines a `__str__` method that returns the `category_name` attribute of an
        object when it is converted to a string.
        :return: The `category_name` attribute of the object is being returned as a string representation
        of the object.
        """
        return self.category_name

    
class Product(TimestampsModel):
    product_name=models.CharField(max_length=100)
    description=models.TextField(max_length=180)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.FileField(upload_to='products/')
    category=models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
   
class Order(TimestampsModel):
    customer_name=models.CharField(max_length=100)
    customer_email=models.EmailField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField()

    def __str__(self):
        return self.customer_name
