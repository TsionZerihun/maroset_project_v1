# Generated by Django 5.0 on 2023-12-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_alter_resume_experience_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='upload_resume',
            field=models.FileField(blank=True, null=True, upload_to='resume'),
        ),
    ]
