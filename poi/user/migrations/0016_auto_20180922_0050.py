# Generated by Django 2.1.1 on 2018-09-22 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_recipeitems_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeitems',
            name='sku',
            field=models.IntegerField(default=0),
        ),
    ]
