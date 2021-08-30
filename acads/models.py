from django.db import models
from datamanager.models import *

# Create your models here.



class subjects(models.Model):
    id = models.AutoField(primary_key=True)
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=50)
    lesson_plan = models.FileField(upload_to='media')
    Semester = models.IntegerField()
    faculty = models.ForeignKey(faculty , on_delete=models.CASCADE,blank=True)
    credit = models.CharField(max_length=10)
    department = models.ForeignKey(department, on_delete=models.CASCADE)

    def __str__(self):
        return self.subjectCode + " "+ self.subjectName

class lectureEnrollment(models.Model):
    id = models.AutoField(primary_key=True)
    lecture = models.ForeignKey(subjects,on_delete=models.CASCADE)
    student = models.ForeignKey(student,on_delete=models.CASCADE)

    def __str__(self):
        return self.student.FullName + " of "+ str(self.student.currentSemester) + " sem Enrolled in " + self.lecture.subjectName


class temporary_subjects(models.Model):
    id = models.AutoField(primary_key=True)
    temporary_subject_code = models.CharField(max_length=15)
    temporary_subject_name = models.CharField(max_length=500)
    semester = models.IntegerField()
    credit = models.CharField(max_length=10)
    temporary_lesson_plan = models.FileField(upload_to='media')
    created_by = models.EmailField()
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    lecture_status = models.CharField(max_length=15)
    changes = models.FileField(upload_to='media')
    last_changes_made_by = models.CharField(max_length=30)
    last_approved_by = models.CharField(max_length=30)
    next_send_to = models.CharField(max_length=15)

class lecture_record(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(subjects,on_delete=models.CASCADE)
    faculty = models.ForeignKey(faculty,on_delete=models.CASCADE)
    goals = models.CharField(max_length=5000)
    status = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.FileField()


class student_status(models.Model):
    student = models.ForeignKey(student,on_delete=models.CASCADE)
    current_semester = models.IntegerField()


class university_session(models.Model):
    