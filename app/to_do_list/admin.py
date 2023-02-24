from django.contrib import admin

from to_do_list.models import ToDo


# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "status", "date")
    list_filter = ("id", "title", "description", "status", "date")
    search_fields = ("title", "description", "status")
    fields = ("title", "description", "status", "date")
    readonly_fields = ("id", "date")


admin.site.register(ToDo, ToDoAdmin)
