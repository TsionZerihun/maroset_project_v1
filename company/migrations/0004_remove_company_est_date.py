# Generated by Django 5.0 on 2023-12-14 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_remove_company_city_remove_company_state_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='est_date',
        ),
    ]
