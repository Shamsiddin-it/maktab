from django.contrib import admin
from .models import Cafedra, Subject, Time, Teacher, Clas, Timetable, Pupil

# Cafedra Admin
@admin.register(Cafedra)
class CafedraAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

# Subject Admin
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('cafedra', 'name',)
    search_fields = ('cafedra__name', 'name',)  # Fixed the foreign key reference
    list_filter = ('cafedra', 'name',)  # Fixed the foreign key reference

# Time Admin
@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('time',)
    search_fields = ('time',)
    list_filter = ('time',)

# Teacher Admin
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'phone', 'email', 'cafedra',)
    search_fields = ('name', 'age', 'phone', 'email', 'cafedra__name',)  # Fixed the foreign key reference
    list_filter = ('cafedra', 'name', 'age', 'phone', 'email',)  # Fixed the foreign key reference

# Clas Admin
@admin.register(Clas)
class ClasAdmin(admin.ModelAdmin):
    list_display = ('grade', 'headteacher',)
    search_fields = ('grade', 'headteacher__name',)  # Fixed the foreign key reference
    list_filter = ('grade', 'headteacher',)

# Timetable Admin
@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('subject', 'clas', 'time', 'teacher',)
    search_fields = ('subject__name', 'clas__grade', 'time__time', 'teacher__name',)
    list_filter = ('subject', 'clas', 'time', 'teacher',)

# Pupil Admin
@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'clas',)
    search_fields = ('name', 'age', 'clas__grade',)  # Fixed the foreign key reference
    list_filter = ('name', 'age', 'clas',)
