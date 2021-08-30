from django.db import models
from acads.models import *
from datamanager.models import *
# Create your models here.


class quiz_info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    quiz_date = models.DateField()
    sstart_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.IntegerField()
    subject = models.ForeignKey(subjects,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class quiz_questions(models.Model):
    id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(quiz_info,on_delete=models.CASCADE)
    question = models.TextField()
    questions_type = models.CharField(max_length=40)
    option1 = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    correct_option = models.CharField(max_length=1000)

    def __str__(self):
        return " "+ self.question + " " + self.option1+ " "+ self.option2+ " "+ self.option3+" "+ self.option4+" "+self.correctOption

class quiz_grades(models.Model):
    id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(quiz_info,on_delete=models.CASCADE)
    student = models.ForeignKey(student,on_delete=models.CASCADE)
    unattempted_questions = models.IntegerField(null=True)
    wrong_answers = models.IntegerField(null=True)
    correct_answers = models.IntegerField(null=True)
    time_taken = models.CharField(max_length=100,null=True,blank=True)
    started_on = models.DateTimeField(null=True,blank=True) 
    submited_on = models.DateTimeField(auto_now_add=True,null=True)
    marks = models.IntegerField()

    def __str__(self):
        return self.quiz.name + " "+ self.student.FullName