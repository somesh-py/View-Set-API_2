# Generated by Django 4.1.5 on 2023-06-24 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('prize', models.CharField(max_length=50)),
            ],
        ),
    ]
