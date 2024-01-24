# Generated by Django 4.1.2 on 2024-01-23 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dist_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.accounttype')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.branches')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.district')),
            ],
        ),
        migrations.AddField(
            model_name='branches',
            name='district_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.district'),
        ),
    ]