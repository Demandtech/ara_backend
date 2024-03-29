# Generated by Django 4.1.7 on 2023-09-08 17:28

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
                ('name', models.CharField(max_length=500)),
                ('category', models.TextField(choices=[('men', 'Men'), ('women', 'Women'), ('accessories', 'Accessories')])),
                ('price', models.FloatField()),
                ('stars', models.FloatField()),
                ('bonus', models.FloatField()),
                ('featured', models.BooleanField(default=False)),
                ('best_seller', models.BooleanField(default=False)),
                ('desc', models.TextField()),
                ('colors', models.JSONField(blank=True, default=list, null=True)),
                ('images', models.JSONField()),
                ('sizes', models.JSONField(blank=True, default=list, null=True)),
            ],
        ),
    ]
