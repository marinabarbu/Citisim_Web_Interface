# Generated by Django 2.2.3 on 2019-07-15 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RTD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energy',
            name='timestamp',
            field=models.CharField(max_length=250),
        ),
    ]
