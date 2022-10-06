from django.db import models

from app.choices import STATE_CHOICES


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100, null=False, blank=False)
    is_actived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    is_actived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    state = models.CharField(choices=STATE_CHOICES, max_length=8, null=False, blank=False)
    description = models.TextField()
    value = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    qty_parcel = models.IntegerField(null=True, blank=True)
    value_parcel = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    cover = models.ImageField(upload_to='app/covers/%Y/%m/', null=True, blank=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
