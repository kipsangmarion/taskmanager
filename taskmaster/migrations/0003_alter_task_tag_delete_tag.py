# Generated by Django 4.2.2 on 2023-07-07 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmaster', '0002_remove_comment_created_at_remove_comment_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tag',
            field=models.CharField(choices=[('UI', 'urgent and important'), ('UNI', 'urgent but not important'), ('NUI', 'not urgent but important'), ('NUNI', 'not urgent and not important')], default=1, max_length=100),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]