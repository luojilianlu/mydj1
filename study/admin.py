from django.contrib import admin
from study.models import Student, Parent

class ParentInLine(admin.StackedInline):
    model = Parent
    extra = 1

class ParentInLineT(admin.TabularInline):
    model = Parent
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    #date_hierarchy = 'add_time'
    list_display = ('name', 'mobile', 'email', 'add_time', 'edit_time', 'colored_name')
    inlines = [ParentInLineT]
    pass

class ParentAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Parent, ParentAdmin)