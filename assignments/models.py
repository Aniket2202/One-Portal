from django.db import models
from acads.models import *
from datamanager.models import *
# Create your models here.

class assignment(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
    ('CA', 'Class'),
    ('HA', 'Home')
]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    assignemnt_type = models.CharField(choices = YEAR_IN_SCHOOL_CHOICES,null=True,max_length=2)
    assignment_file = models.FileField()
    subject = models.ForeignKey(subjects,on_delete=models.CASCADE)
    starting_date = models.DateField(null=True)
    deadline = models.DateField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class assignmentSubmission(models.Model):
    id = models.AutoField(primary_key=True)
    assignment = models.ForeignKey(assignment,on_delete=models.CASCADE)
    submission_file = models.FileField()
    submited_by = models.ForeignKey(student,on_delete=models.CASCADE)
    submited_on = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(blank=True,null=True)
    def __str__(self) -> str:
        return str(self.id)+" " + self.assignment.name +" "+ self.assignment.subject.subjectName+ " " + self.submitedBy.FullName
