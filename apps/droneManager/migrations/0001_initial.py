# Generated by Django 3.1.1 on 2020-09-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('speed', models.DecimalField(decimal_places=1, max_digits=6)),
                ('altimeter', models.IntegerField()),
                ('task', models.CharField(max_length=50)),
            ],
        ),
    ]
