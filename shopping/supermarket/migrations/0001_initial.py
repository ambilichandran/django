# Generated by Django 5.0.7 on 2024-08-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=None, max_length=100)),
                ('price', models.IntegerField(blank=None)),
                ('image', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
