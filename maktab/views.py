from django.views.generic import ListView, TemplateView, CreateView
from .models import Cafedra, Subject, Time, Teacher, Clas, Timetable, Pupil
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout ,authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


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

class ClasListView(PermissionRequiredMixin, ListView):
    model = Clas
    template_name = 'clas_list.html'
    context_object_name = 'clases'
    permission_required = 'maktab.view_clas'
    permission_denied_message = "You dont have permissions to see classses"

    

class TimetableListView(ListView):
    model = Timetable
    template_name = 'timetable_list.html'
    context_object_name = 'timetables'

class PupilListView(ListView):
    model = Pupil
    template_name = 'pupil_list.html'
    context_object_name = 'pupils'

class HomeView(TemplateView):
    template_name = "home.html"




def gt_2(request):
    pupils = Pupil.objects.filter(clas__grade__gt='2') 
    return render(request, 'gt_2.html', {'pupils': pupils})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class PupilCreateView(CreateView):
    model = Pupil
    template_name = "pupil_create.html"
    fields = ['name', 'age', 'clas']
    success_url = reverse_lazy('pupil_list')

class ClasCreateView(CreateView):
    model = Clas
    template_name = "clas_create.html"
    fields = ['grade', 'headteacher']
    success_url = reverse_lazy('clas_list')

