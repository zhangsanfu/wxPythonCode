# Generated by Django 2.0.1 on 2018-11-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_emp'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comment_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]