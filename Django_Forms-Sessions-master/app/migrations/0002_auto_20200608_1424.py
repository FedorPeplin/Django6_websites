# Generated by Django 2.2.10 on 2020-06-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.FileField(upload_to='products/%Y/%m/%d/'),
        ),
    ]
