from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


class Category(MPTTModel, models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name_plural = 'Categories'

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by=['name']


    def __str__(self):
        return str(self.name)


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=255, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    Barcode  = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to='images/thumbnails/%Y/%m/%d')

    def __str__(self):
        return str(self.title)


class ItemAlbum(models.Model):
    post = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE, null=False, blank=True)
    image = models.ImageField(upload_to='images/albums/%Y/%m/%d')