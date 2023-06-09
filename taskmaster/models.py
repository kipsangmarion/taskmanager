from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_in_profile')
    registered_at = models.DateTimeField()
    last_login = models.DateTimeField()
    intro = models.TextField()
    image = models.ImageField()


TASK_STATUSES = (
    ('NEW', 'new'),
    ('IN-PROGRESS', 'in-progress'),
    ('COMPLETED', 'completed')
)

TASK_TAGS = (
    ('U&I', 'urgent and important'),
    ('U&NI', 'urgent but not important'),
    ('NU&I', 'not urgent but important'),
    ('NU&NI', 'not urgent and not important')
)


class Tag(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    tag = models.CharField(
        max_length=100,
        choices=TASK_TAGS,
        default=1
    )


class Task(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_in_task')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_by')
    title = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag_in_task')
    desc = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TASK_STATUSES,
        default=1
    )
    hours = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    planned_start_date = models.DateTimeField()
    planned_end_date = models.DateTimeField()
    actual_start_date = models.DateTimeField()
    actual_end_date = models.DateTimeField()
    content = models.TextField()


ACTIVITY_STATUSES = (
    ('NEW', 'new'),
    ('IN-PROGRESS', 'in-progress'),
    ('COMPLETED', 'completed')
)


class Activity(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_in_activity')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_by')
    title = models.TextField()
    desc = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TASK_STATUSES,
        default=1
    )
    hours = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    planned_start_date = models.DateTimeField()
    planned_end_date = models.DateTimeField()
    actual_start_date = models.DateTimeField()
    actual_end_date = models.DateTimeField()
    content = models.TextField()


class Comment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    task = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_in_task')
    activity = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_in_activity')
    title = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    content = models.TextField()
