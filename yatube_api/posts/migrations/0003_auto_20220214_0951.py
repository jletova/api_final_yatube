# Generated by Django 2.2.16 on 2022-02-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220210_1605'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(following__isnull=False), name='fallowing_not_null'),
        ),
    ]
