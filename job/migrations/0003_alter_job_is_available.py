# Generated by Django 5.0 on 2023-12-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
