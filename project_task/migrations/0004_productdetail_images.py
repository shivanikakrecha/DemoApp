# Generated by Django 2.2.11 on 2020-08-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_task', '0003_auto_20200829_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]