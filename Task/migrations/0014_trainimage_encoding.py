# Generated by Django 3.0.7 on 2020-07-03 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0013_auto_20200702_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainimage',
            name='encoding',
            field=models.BinaryField(default=None),
        ),
    ]
