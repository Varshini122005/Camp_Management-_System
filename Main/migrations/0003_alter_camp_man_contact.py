# Generated by Django 4.2.2 on 2023-08-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_camp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='man_contact',
            field=models.IntegerField(),
        ),
    ]
