# Generated by Django 4.1.4 on 2022-12-09 23:18

import KetoGo.core.model_mixin
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('salad', 'Salad'), ('sandwich', 'Sandwich'), ('chaffle', 'Chaffle'), ('dessert', 'Dessert')], max_length=8)),
                ('product_photo', models.ImageField(blank=True, upload_to='product_photos/')),
                ('description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
            bases=(KetoGo.core.model_mixin.StrFromFieldMixin, models.Model),
        ),
    ]