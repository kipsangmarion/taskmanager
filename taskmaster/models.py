from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_in_profile')
    intro = models.TextField()
    image = models.ImageField()


TASK_STATUSES = (
    ('NEW', 'new'),
    ('INPROGRESS', 'in-progress'),
    ('COMPLETED', 'completed')
)

TASK_TAGS = (
    ('UI', 'urgent and important'),
    ('UNI', 'urgent but not important'),
    ('NUI', 'not urgent but important'),
    ('NUNI', 'not urgent and not important')
)


class Task(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_in_task')
    title = models.TextField()
    tag = models.CharField(
        max_length=100,
        choices=TASK_TAGS,
        default=1
    )
    desc = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TASK_STATUSES,
        default=1,null=True
    )
    hours = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    planned_start_date = models.DateTimeField(null=False, blank=False)
    planned_end_date = models.DateTimeField(null=False, blank=False)
    actual_start_date = models.DateTimeField(null=False, blank=False)
    actual_end_date = models.DateTimeField(null=False, blank=False)
    content = models.TextField()


ACTIVITY_STATUSES = (
    ('NEW', 'new'),
    ('INPROGRESS', 'inprogress'),
    ('COMPLETED', 'completed')
)


class Activity(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='activity_in_task')
    title = models.TextField()
    desc = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TASK_STATUSES,
        default=1,
        null=True
    )
    hours = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


class Comment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comment_in_task',null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='comment_in_activity',null=True)
    content = models.TextField()
