# Generated by Django 5.0 on 2023-12-14 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_rename_job_title_resume_experience_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='location',
        ),
    ]
