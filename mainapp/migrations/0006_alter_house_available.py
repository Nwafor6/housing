# Generated by Django 4.1.7 on 2023-02-21 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_house_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='available',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30),
        ),
    ]