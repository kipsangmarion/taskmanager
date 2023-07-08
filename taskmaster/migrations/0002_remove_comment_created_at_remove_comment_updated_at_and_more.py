# Generated by Django 4.2.2 on 2023-07-07 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmaster', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='registered_at',
        ),
        migrations.AlterField(
            model_name='activity',
            name='status',
            field=models.CharField(choices=[('NEW', 'new'), ('INPROGRESS', 'in-progress'), ('COMPLETED', 'completed')], default=1, max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('NEW', 'new'), ('INPROGRESS', 'in-progress'), ('COMPLETED', 'completed')], default=1, max_length=20),
        ),
    ]
