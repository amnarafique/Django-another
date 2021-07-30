from django.contrib import admin

from tasks.models import Task

# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'dead_line', 'done',
                    'date_created', 'date_modified']

    list_editable = ['title']
    list_display_links = ['dead_line']
    list_filter = ['date_created', 'date_modified','dead_line','done']
    search_fields = ['title', 'description']
