# Generated by Django 3.0.8 on 2020-09-26 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0024_auto_20200926_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='qty',
        ),
    ]
