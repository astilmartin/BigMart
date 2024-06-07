# Generated by Django 5.0.4 on 2024-05-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=500, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Product Images')),
            ],
        ),
    ]
