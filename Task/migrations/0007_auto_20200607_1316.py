# Generated by Django 3.0.7 on 2020-06-07 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0006_auto_20200607_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskName',
            field=models.TextField(default=None),
        ),
    ]