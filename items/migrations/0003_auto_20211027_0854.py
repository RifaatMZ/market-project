# Generated by Django 3.1.2 on 2021-10-27 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20211027_0845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='test', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
