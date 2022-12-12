# Generated by Django 4.1.4 on 2022-12-10 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_alter_product_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=300)),
                ('date_and_time_of_publication', models.DateField(auto_now_add=True)),
                ('to_product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_and_time_of_publication'],
            },
        ),
    ]
