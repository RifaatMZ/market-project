# Generated by Django 3.1.2 on 2021-10-25 12:38

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('mptt_level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shops.location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=225)),
                ('description', models.TextField(max_length=1020)),
                ('phone', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('logo', models.ImageField(upload_to='shops/logos/%Y/%m/%d')),
                ('image', models.ImageField(upload_to='shops/image/%Y/%m/%d')),
                ('delevery_zone', models.ManyToManyField(related_name='Location', to='shops.Location')),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shops.location')),
            ],
        ),
        migrations.CreateModel(
            name='ShopAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shops/albums/%Y/%m/%d')),
                ('shop', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shops.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('quantity', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='items.itemtemplate')),
                ('shop', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=128)),
                ('telegram', models.CharField(max_length=128)),
                ('whatsapp', models.CharField(max_length=128)),
                ('viber', models.CharField(max_length=128)),
                ('shop', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
    ]