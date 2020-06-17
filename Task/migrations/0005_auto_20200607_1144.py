# Generated by Django 3.0.7 on 2020-06-07 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0004_auto_20200606_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='userReference',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Task.User'),
        ),
    ]