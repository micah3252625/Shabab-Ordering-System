# Generated by Django 3.0.8 on 2020-09-19 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20200919_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaPromo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='account/images/')),
                ('promo_name', models.CharField(max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AlterField(
            model_name='pizza',
            name='base_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
