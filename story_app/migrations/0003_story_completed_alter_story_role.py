# Generated by Django 5.0.3 on 2024-04-05 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story_app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='completed',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='role',
            field=models.CharField(blank=True, null=True),
        ),
    ]
