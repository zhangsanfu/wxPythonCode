# Generated by Django 2.0.1 on 2019-03-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_permission_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='路径别名'),
        ),
    ]