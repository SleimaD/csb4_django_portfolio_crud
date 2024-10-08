# Generated by Django 4.2.11 on 2024-05-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, max_length=200)),
                ('profile_image', models.ImageField(upload_to='images/')),
                ('general_description', models.TextField()),
                ('birthday', models.DateField()),
                ('website', models.URLField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('degree', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('freelance', models.CharField(max_length=100)),
                ('detailed_description', models.TextField()),
            ],
        ),
    ]
