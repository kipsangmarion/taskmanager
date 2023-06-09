from django.contrib import admin

from .models import UserProfile
from .models import Task
from .models import Tag
from .models import Activity
from .models import Comment

admin.site.register(UserProfile)
admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Activity)
admin.site.register(Comment)
