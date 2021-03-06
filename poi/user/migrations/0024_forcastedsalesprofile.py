# Generated by Django 2.1.1 on 2018-09-24 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_delete_salesprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForcastedSalesProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('monday', models.FloatField(default=0)),
                ('tuesday', models.FloatField(default=0)),
                ('wednesday', models.FloatField(default=0)),
                ('thursday', models.FloatField(default=0)),
                ('friday', models.FloatField(default=0)),
                ('saturday', models.FloatField(default=0)),
                ('sunday', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
            ],
        ),
    ]
