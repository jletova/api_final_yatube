# Generated by Django 2.2.16 on 2022-02-14 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20220214_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={},
        ),
        migrations.RemoveConstraint(
            model_name='comment',
            name='unique_comment',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follow',
        ),
    ]