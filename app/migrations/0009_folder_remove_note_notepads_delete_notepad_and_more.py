# Generated by Django 4.1.4 on 2022-12-26 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_notepad_remove_note_folders_delete_folder_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4)),
                ('title', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
        migrations.RemoveField(
            model_name='note',
            name='notepads',
        ),
        migrations.DeleteModel(
            name='Notepad',
        ),
        migrations.AddField(
            model_name='note',
            name='folders',
            field=models.ManyToManyField(blank=True, to='app.folder'),
        ),
    ]
