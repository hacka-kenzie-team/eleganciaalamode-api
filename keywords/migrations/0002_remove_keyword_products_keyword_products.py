# Generated by Django 4.2.7 on 2023-11-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('keywords', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='products',
        ),
        migrations.AddField(
            model_name='keyword',
            name='products',
            field=models.ManyToManyField(related_name='keywords', to='products.product'),
        ),
    ]
