# Generated by Django 4.1.4 on 2022-12-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_note_deleted_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AddField(
            model_name='note',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
