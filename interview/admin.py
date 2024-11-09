
from django.contrib import admin
from .models import InterviewRound

@admin.register(InterviewRound)
class InterviewRoundAdmin(admin.ModelAdmin):
    list_display = ('round_number', 'round_type', 'created_at')
    list_filter = ('round_type', 'created_at')
    search_fields = ('round_number', 'round_type')
    ordering = ('round_number',)