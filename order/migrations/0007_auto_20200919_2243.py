# Generated by Django 3.0.8 on 2020-09-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20200919_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='base_price',
            field=models.DecimalField(decimal_places=2, default=140, max_digits=6),
        ),
    ]