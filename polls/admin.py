from django.contrib import admin

from .models import Question, Choice, PollUser, UserLog

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(PollUser)
admin.site.register(UserLog)

# Register your models here.
