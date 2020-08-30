# Generated by Django 2.2.11 on 2020-08-29 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=30, verbose_name='Brand name')),
                ('description', models.TextField(max_length=500, verbose_name='Brand description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=30, verbose_name='Category name')),
                ('description', models.TextField(max_length=500, verbose_name='Category description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=30, verbose_name='Product name')),
                ('description', models.TextField(max_length=500, verbose_name='Product description')),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('is_avialable', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_task.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_task.Category')),
                ('colors', models.ManyToManyField(blank=True, null=True, to='project_task.Color')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
