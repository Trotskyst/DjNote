# Generated by Django 2.2 on 2019-05-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20190429_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=200, null=True),
        ),
    ]