# Generated by Django 3.0.5 on 2021-05-26 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RUC', '0004_auto_20210526_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruc',
            name='rucEmpresa',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
