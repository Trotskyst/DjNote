# Generated by Django 2.2 on 2019-05-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_remove_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='label',
            field=models.CharField(max_length=200, unique=True, verbose_name='Тег'),
        ),
    ]