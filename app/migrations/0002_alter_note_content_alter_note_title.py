# Generated by Django 4.1.4 on 2022-12-15 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]
