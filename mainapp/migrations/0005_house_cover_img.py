# Generated by Django 4.1.7 on 2023-02-20 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_rename_lodge_name_house_lodge_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='cover_img',
            field=models.ImageField(blank=True, null=True, upload_to='lodge_cover_img'),
        ),
    ]
