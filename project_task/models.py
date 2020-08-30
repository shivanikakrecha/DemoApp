from django.db import models

# Create your models here.


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)

    class Meta:
        abstract = True


class Color(TimeStampModel, models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Brand(TimeStampModel, models.Model):
    name = models.CharField(max_length=30, verbose_name='Brand name')
    description = models.TextField(
        max_length=500, verbose_name='Brand description')

    def __str__(self):
        return self.name


class Category(TimeStampModel, models.Model):
    name = models.CharField(max_length=30, verbose_name='Category name')
    description = models.TextField(
        max_length=500, verbose_name='Category description')

    def __str__(self):
        return self.name


class Product(TimeStampModel, models.Model):
    name = models.CharField(max_length=30, verbose_name='Product name')
    description = models.TextField(
        max_length=500, verbose_name='Product description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class ProductDetail(TimeStampModel, models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(
        upload_to='product_images/',  null=True, blank=True)
    quantity = models.IntegerField(default=0)
    is_avialable = models.BooleanField(default=True)
    colors = models.ForeignKey(
        Color, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.product.name) + ' has quantity ' + str(self.quantity)
