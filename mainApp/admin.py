from django.contrib import admin

# Register your models here.
from .models import user,question,answer
admin.site.register(user)
admin.site.register(question)
admin.site.register(answer)