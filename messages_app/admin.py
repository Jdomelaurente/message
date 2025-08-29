from django.contrib import admin
from .models import Message  # import your model

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'content', 'created_at')  # choose fields to display
