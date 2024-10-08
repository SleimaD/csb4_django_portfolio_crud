# Generated by Django 4.2.11 on 2024-05-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('street', models.CharField(max_length=200)),
                ('street_number', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
