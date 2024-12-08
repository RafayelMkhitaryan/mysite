from django.contrib import admin
from .models import Question, Choice, PollUser

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(PollUser)
# Register your models here.
