# Generated by Django 4.1.2 on 2024-01-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0003_userdetails_materials'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='materials_provide',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
