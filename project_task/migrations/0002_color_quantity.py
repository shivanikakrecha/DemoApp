# Generated by Django 2.2.11 on 2020-08-29 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
