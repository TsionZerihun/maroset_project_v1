# Generated by Django 5.0 on 2024-01-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_conversationmessageuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='jobname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
