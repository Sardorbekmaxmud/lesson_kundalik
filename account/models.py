from django.db import models
from datetime import datetime

# Create your models here.
class PersonModel(models.Model):
    name = models.CharField(max_length=65,default='')
    fname = models.CharField(max_length=65,default='')
    date_of_birth =models.DateField(default=datetime.now)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True

class ParentsModel(PersonModel):
    user_name = models.CharField(max_length=65,default='')
    password = models.CharField(max_length=40,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'parent'

class StudentModel(PersonModel):
    # from school.models import SchoolModel,ClassModel
    school = models.ForeignKey('school.SchoolModel',on_delete=models.CASCADE)
    clasS = models.ForeignKey('school.ClassModel',on_delete=models.SET_NULL,null=True)
    parents = models.ForeignKey(ParentsModel,default='',on_delete=models.SET_NULL,null=True)
    username = models.CharField(max_length=65,default='')
    password = models.CharField(max_length=40,default='')
    avtive = models.BooleanField(default=True)
    phone = models.CharField(max_length=13,default='')

    def __str__(self):
        return f"{self.name} {self.fname}"

    class Meta:
        db_table = 'student'


class TeacherModel(PersonModel):
    # from school.models import SchoolModel
    # from statistic.models import SubjectModel
    subject = models.ForeignKey('statistic.SubjectModel',on_delete=models.CASCADE)
    TOIFA_TEACHER = (
        ("OM","Oliy Ma'lumot"),
        ("OR","O'rta Ma'lumot"),
        ("OP","O'qituvchi Pedagok"),
    )
    toifa = models.CharField(max_length=2,choices=TOIFA_TEACHER,default='')
    salary = models.PositiveIntegerField(default=1)
    school = models.ManyToManyField('school.SchoolModel')

    def __str__(self):
        return f"{self.name} {self.fname}"

    class Meta:
        db_table = 'teacher'
