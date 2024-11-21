# Generated by Django 5.1.1 on 2024-11-18 12:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField()),
                ('size', models.IntegerField()),
                ('bio', models.CharField()),
                ('employees_number', models.IntegerField()),
                ('establishment_date', models.DateTimeField()),
                ('git_link', models.CharField(blank=True, null=True)),
                ('linkedIn_link', models.CharField(blank=True, null=True)),
                ('x_link', models.CharField(blank=True, null=True)),
                ('website_link', models.CharField(blank=True, null=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
