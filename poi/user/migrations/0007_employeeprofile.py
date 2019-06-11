# Generated by Django 2.1.1 on 2018-09-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180919_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(blank=True, max_length=110)),
                ('last', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('employee_number', models.CharField(default='', max_length=50)),
                ('phone', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
