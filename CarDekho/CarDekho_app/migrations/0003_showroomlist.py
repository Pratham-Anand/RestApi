# Generated by Django 3.2.6 on 2024-02-08 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarDekho_app', '0002_auto_20240207_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showroomlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('website', models.URLField(max_length=100)),
            ],
        ),
    ]