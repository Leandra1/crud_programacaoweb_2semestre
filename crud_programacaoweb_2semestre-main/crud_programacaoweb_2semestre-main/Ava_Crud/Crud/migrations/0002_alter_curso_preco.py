# Generated by Django 4.1 on 2022-08-31 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]