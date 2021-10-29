from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from items.models import Item
from django.contrib.auth.models import User


# Create your models here.
class Location(MPTTModel, models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by=['name']

    def __str__(self):
        return str(self.name)


class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False, blank=True)
    delevery_zone = models.ManyToManyField(Location, related_name='Location')
    address = models.CharField(max_length=225)
    description = models.TextField(max_length=1020)
    phone = models.CharField(max_length=32)
    email = models.EmailField()
    logo = models.ImageField(upload_to='shops/logos/%Y/%m/%d')
    image = models.ImageField(upload_to='shops/image/%Y/%m/%d')

    def __str__(self):
        return str(self.name)
    

class ShopAlbum(models.Model):
    shop = models.ForeignKey(Shop, related_name='images', on_delete=models.CASCADE, null=False, blank=True)
    image = models.ImageField(upload_to='shops/albums/%Y/%m/%d')


class Contacts(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=True)
    facebook = models.CharField(max_length=128)
    telegram = models.CharField(max_length=128)
    whatsapp = models.CharField(max_length=128)
    viber = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Contacts'


class ItemDetail(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    in_stock = models.BooleanField(default=False)
    quantity = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item)