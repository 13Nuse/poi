# Generated by Django 2.1.1 on 2018-09-22 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_recipeitems_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeitems',
            name='description',
        ),
        migrations.AlterField(
            model_name='recipeitems',
            name='category',
            field=models.CharField(choices=[('RAW', 'raw'), ('FRESH', 'fresh'), ('DAIRY', 'dairy'), ('PREP', 'prep'), ('SPICE', 'spice'), ('APPS', 'apps'), ('ENTREE', 'entree')], default='prep', max_length=15),
        ),
    ]
