# Generated by Django 3.2.7 on 2021-09-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
    ]
