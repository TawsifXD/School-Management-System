# Generated by Django 4.1.4 on 2022-12-10 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_subject_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session_year',
            old_name='session_stats',
            new_name='session_starts',
        ),
    ]