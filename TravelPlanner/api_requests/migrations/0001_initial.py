# Generated by Django 4.1.6 on 2023-02-14 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spanish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=200)),
                ('spanish', models.CharField(max_length=200)),
            ],
        ),
    ]
