# Generated by Django 2.0.6 on 2018-11-13 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchurl',
            name='fetch_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
