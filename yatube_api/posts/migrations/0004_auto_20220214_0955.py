# Generated by Django 2.2.16 on 2022-02-14 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220214_0951'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='fallowing_not_null',
        ),
    ]