# Generated by Django 3.1.2 on 2021-12-03 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20211202_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='creator',
            field=models.CharField(max_length=255),
        ),
    ]
