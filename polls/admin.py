
# Register your models here.
from django.contrib import admin

from .models import Question, Choice, Quote

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Quote)
