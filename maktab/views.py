from django.views.generic import ListView
from .models import Cafedra, Subject, Time, Teacher, Clas, Timetable, Pupil
from django.shortcuts import render


class CafedraListView(ListView):
    model = Cafedra
    template_name = 'cafedra_list.html'
    context_object_name = 'cafedras'

class SubjectListView(ListView):
    model = Subject
    template_name = 'subject_list.html'
    context_object_name = 'subjects'

class TimeListView(ListView):
    model = Time
    template_name = 'time_list.html'
    context_object_name = 'times'

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'
    context_object_name = 'teachers'

class ClasListView(ListView):
    model = Clas
    template_name = 'clas_list.html'
    context_object_name = 'clases'

class TimetableListView(ListView):
    model = Timetable
    template_name = 'timetable_list.html'
    context_object_name = 'timetables'

class PupilListView(ListView):
    model = Pupil
    template_name = 'pupil_list.html'
    context_object_name = 'pupils'




def gt_2(request):
    pupils = Pupil.objects.filter(clas__grade__gt='2') 
    return render(request, 'gt_2.html', {'pupils': pupils})
