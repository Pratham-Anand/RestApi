# Generated by Django 3.2.6 on 2024-02-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarDekho_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='chassisnumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carlist',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]