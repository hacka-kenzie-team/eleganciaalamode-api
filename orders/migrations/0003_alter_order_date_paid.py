# Generated by Django 4.2.7 on 2023-11-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_paid',
            field=models.DateField(auto_now_add=True),
        ),
    ]