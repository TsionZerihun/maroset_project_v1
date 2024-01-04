# Generated by Django 5.0 on 2024-01-04 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_rename_founder_startup_user'),
        ('job', '0011_conversationmessagejob'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='startup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.startup'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.company'),
        ),
    ]
