# Generated by Django 4.2.2 on 2023-07-07 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmaster', '0003_alter_task_tag_delete_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='actual_end_date',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='actual_start_date',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='planned_end_date',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='planned_start_date',
        ),
    ]
