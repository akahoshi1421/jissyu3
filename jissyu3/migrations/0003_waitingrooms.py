# Generated by Django 3.2.5 on 2022-08-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jissyu3', '0002_alter_waitngusers_usernum'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaitingRooms',
            fields=[
                ('roomName', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]