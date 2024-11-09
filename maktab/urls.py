from django.urls import path
from .views import *

urlpatterns = [
    path('cafedra/', CafedraListView.as_view(), name='cafedra_list'),
    path('subject/', SubjectListView.as_view(), name='subject_list'),
    path('time/', TimeListView.as_view(), name='time_list'),
    path('teacher/', TeacherListView.as_view(), name='teacher_list'),
    path('clas/', ClasListView.as_view(), name='clas_list'),
    path('timetable/', TimetableListView.as_view(), name='timetable_list'),
    path('pupil/', PupilListView.as_view(), name='pupil_list'),
    path('students/above-grade-2/', gt_2, name='gt_2'),
]

