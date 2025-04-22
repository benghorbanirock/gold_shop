from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class gold_hand(models.Model):
    name=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='products/')
    description=models.TextField()
    weight=models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=50, choices=[('gold', 'Gold'), ('silver', 'Silver')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('unavailable', 'Unavailable')])
    rating = models.FloatField(default=0.0)
    review_count = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, default="Unknown")
    sku = models.CharField(max_length=50, unique=True)
    is_discounted = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    packaging = models.CharField(max_length=100)
    warranty = models.CharField(max_length=100, blank=True)
    additional_info = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name

class gold_ring(models.Model):
    name=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='products/')
    description=models.TextField()
    weight=models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=50, choices=[('gold', 'Gold'), ('silver', 'Silver')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('unavailable', 'Unavailable')])
    rating = models.FloatField(default=0.0)
    review_count = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, default="Unknown")
    sku = models.CharField(max_length=50, unique=True)
    is_discounted = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    packaging = models.CharField(max_length=100)
    warranty = models.CharField(max_length=100, blank=True)
    additional_info = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name
class gold_goshvareh(models.Model):
    name=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='products/')
    description=models.TextField()
    weight=models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=50, choices=[('gold', 'Gold'), ('silver', 'Silver')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('unavailable', 'Unavailable')])
    rating = models.FloatField(default=0.0)
    review_count = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, default="Unknown")
    sku = models.CharField(max_length=50, unique=True)
    is_discounted = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    packaging = models.CharField(max_length=100)
    warranty = models.CharField(max_length=100, blank=True)
    additional_info = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name

class silver_hand(models.Model):
    name=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='products/')
    description=models.TextField()
    weight=models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=50, choices=[('gold', 'Gold'), ('silver', 'Silver')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('unavailable', 'Unavailable')])
    rating = models.FloatField(default=0.0)
    review_count = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, default="Unknown")
    sku = models.CharField(max_length=50, unique=True)
    is_discounted = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    packaging = models.CharField(max_length=100)
    warranty = models.CharField(max_length=100, blank=True)
    additional_info = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name

class silver_ring(models.Model):
    name=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='products/')
    description=models.TextField()
    weight=models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=50, choices=[('gold', 'Gold'), ('silver', 'Silver')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('unavailable', 'Unavailable')])
    rating = models.FloatField(default=0.0)
    review_count = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, default="Unknown")
    sku = models.CharField(max_length=50, unique=True)
    is_discounted = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    packaging = models.CharField(max_length=100)
    warranty = models.CharField(max_length=100, blank=True)
    additional_info = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name

class silver_goshvareh(models.Model):
    name=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='products/')
    description=models.TextField()
    weight=models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=50, choices=[('gold', 'Gold'), ('silver', 'Silver')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('unavailable', 'Unavailable')])
    rating = models.FloatField(default=0.0)
    review_count = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, default="Unknown")
    sku = models.CharField(max_length=50, unique=True)
    is_discounted = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    packaging = models.CharField(max_length=100)
    warranty = models.CharField(max_length=100, blank=True)
    additional_info = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name

class stones(models.Model):
    name=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='products/')
    description=models.TextField()
    weight=models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=50, choices=[('ruby', 'Ruby'),
                                                         ('sapphire', 'Sapphire'), ('aquamarine', 'Aquamarine'), ('diamond', 'Diamond'), ('emerald', 'Emerald'), ('white topaz', 'White Topaz'), ('moon stone', 'Moon Stone'), ('citrine', 'Citrine')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('unavailable', 'Unavailable')])
    rating = models.FloatField(default=0.0)
    review_count = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, default="Unknown")
    sku = models.CharField(max_length=50, unique=True)
    is_discounted = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    packaging = models.CharField(max_length=100)
    warranty = models.CharField(max_length=100, blank=True)
    additional_info = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name