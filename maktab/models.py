from django.db import models

class Cafedra(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Subject(models.Model):
    cafedra = models.ForeignKey(Cafedra, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Time(models.Model):
    time = models.CharField(max_length=50)
    def __str__(self):
        return self.time

class Teacher(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True, blank=True)
    cafedra = models.ForeignKey(Cafedra, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Clas(models.Model):
    GRADE = (
        ("1", '1'),
        ("2", '2'),
        ("3", '3'),
        ("4", '4'),
        ("5", '5'),
        ("6", '6'),
        ("7", '7'),
        ("8", '8'),
        ("9", '9'),
        ("10", '10'),
        ("11", '11'),
    )
    grade = models.CharField(choices=GRADE, max_length=50)
    headteacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return self.grade

class Timetable(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    WEEKDAY = (
        ("Mon", "Mon"),
        ("Tue", "Tue"),
        ("Wed", "Wed"),
        ("Thu", "Thu"),
        ("Fri", "Fri"),
        ("Sat", "Sat"),
    )
    weekday = models.CharField(choices=WEEKDAY, max_length=50)  # Fixed the typo here
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Pupil(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
