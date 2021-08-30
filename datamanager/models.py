from django.db import models
from django.conf import settings
from acads.models import *

# Create your models here.

class employee(models.Model):
    id = models.AutoField(primary_key=True)
    employeeID = models.CharField(max_length=10)
    personalEmail = models.EmailField()
    universityEmail = models.EmailField(blank=True)
    Name = models.CharField(max_length=20)
    Dob = models.DateField()
    Doj = models.DateField()


    def __str__(self):
        return self.Name

class school(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dean = models.ForeignKey(employee,on_delete=models.CASCADE)
    status = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)


class program(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    school = models.ForeignKey(school,on_delete=models.CASCADE)
    total_semester = models.IntegerField(blank=True)
    status = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class department(models.Model):
    id = models.AutoField(primary_key=True)
    department_code = models.CharField(max_length=10)
    department_name = models.CharField(max_length=100)
    head_of_department = models.ForeignKey(employee,on_delete=models.CASCADE)
    specialized_course = models.BooleanField()
    start_date = models.DateField()
    School = models.ForeignKey(school,on_delete=models.CASCADE)
    Status = models.BooleanField()

    def __str__(self):
        return self.department_id

class faculty(models.Model):
    id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(employee,on_delete=models.CASCADE)
    department = models.ForeignKey(department,on_delete=models.CASCADE)

    def __str__(self):
        return self.FacultyID.Name

class student(models.Model):#Student Information
    id = models.AutoField(primary_key=True)
    enrollment_number = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    program = models.ForeignKey(program,on_delete=models.CASCADE)
    batch_year = models.CharField(max_length=10)
    university_email_id = models.CharField(max_length=100)
    personal_email_id = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    # current_semester = models.IntegerField(blank=True)
    street_address = models.CharField(max_length=100)
    district = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()
    last_qualification = models.CharField(max_length=100)


    def __str__(self):
        return self.EnrollmentNumber


# class modes(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     createdOn = models.DateTimeField(auto_now_add=True)
#     updatedOn = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

# class weightage(models.Model):
#     id = models.AutoField(primary_key=True)
#     mode = models.ForeignKey('modes',on_delete=models.CASCADE)
#     subjects = models.ForeignKey(subjects,on_delete=models.CASCADE)
#     percentage = models.CharField(max_length=5)
#     assignedBy = models.ForeignKey(faculty,on_delete=models.CASCADE)
#     validTill = models.DateField(null=True,blank=True)
#     assignedOn = models.DateTimeField()

#     def __str__(self):
#         return self.mode.name + " - " + self.percentage + "%"



# class attendance(models.Model):
#     id = models.AutoField(primary_key=True)
#     attendies = models.ForeignKey(student,on_delete=models.CASCADE)
#     subject = models.ForeignKey(subjects,on_delete=models.CASCADE)
#     takenOn = models.DateTimeField(auto_now_add=True)

# c


