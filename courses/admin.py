from django.contrib import admin
from .models import Course,Chapter,Enrollment
# Register your models here.
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter_number', 'course')
    search_fields = ('title', 'course__name')
    list_filter = ('course',)
    
admin.site.register(Course)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Enrollment)