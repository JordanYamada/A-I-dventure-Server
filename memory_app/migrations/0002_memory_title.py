# Generated by Django 5.0.3 on 2024-04-13 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='title',
            field=models.CharField(blank=True, null=True),
        ),
    ]
