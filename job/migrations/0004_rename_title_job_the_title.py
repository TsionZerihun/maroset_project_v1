# Generated by Django 5.0 on 2023-12-18 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_is_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='title',
            new_name='the_title',
        ),
    ]
