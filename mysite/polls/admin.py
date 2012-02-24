from mysite.polls.models import Poll
from mysite.polls.models import Choice
from django.contrib import admin

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    
    list_filter = ['pub_date']
    list_display = ('question', 'pub_date', 'was_published_today')
    inlines= [ChoiceInLine]

admin.site.register(Poll, PollAdmin)
