# Generated by Django 4.1.4 on 2022-12-18 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='initials',
            field=models.CharField(default='SK', max_length=3),
            preserve_default=False,
        ),
    ]
