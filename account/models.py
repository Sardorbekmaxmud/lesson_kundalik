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

class SubjectModel(models.Model):
    name = models.CharField(max_length=67,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'

class SchoolModel(models.Model):
    number = models.PositiveSmallIntegerField(default=1)
    address = models.CharField(max_length=200,default='')
    info = models.JSONField()

    def __str__(self):
        return f"{self.number}"

    class Meta:
        db_table = 'school'

class ClassModel(models.Model):
    name = models.CharField(max_length=4,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'class'

class ParentsModel(PersonModel):
    user_name = models.CharField(max_length=65,default='')
    password = models.CharField(max_length=40,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'parent'

class StudentModel(PersonModel):
    school = models.ForeignKey(SchoolModel,on_delete=models.CASCADE)
    clasS = models.ForeignKey(ClassModel,on_delete=models.SET_NULL,null=True)
    parents = models.ForeignKey(ParentsModel,default='',on_delete=models.SET_NULL,null=True)
    user_name = models.CharField(max_length=65,default='')
    password = models.CharField(max_length=40,default='')
    avtive = models.BooleanField(default=True)
    phone = models.CharField(max_length=13,default='')

    def __str__(self):
        return f"{self.name} {self.fname}"

    class Meta:
        db_table = 'student'


class TeacherModel(PersonModel):
    subject = models.ForeignKey(SubjectModel,on_delete=models.CASCADE)
    TOIFA_TEACHER = (
        ("OM","Oliy Ma'lumot"),
        ("OR","O'rta Ma'lumot"),
        ("OP","O'qituvchi Pedagok"),
    )
    toifa = models.CharField(max_length=2,choices=TOIFA_TEACHER,default='')
    salary = models.PositiveIntegerField(default=1)
    school = models.ManyToManyField(SchoolModel)

    def __str__(self):
        return f"{self.name} {self.fname}"

    class Meta:
        db_table = 'teacher'

class AttendanceModel(models.Model):
    student = models.ForeignKey(StudentModel,on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherModel,on_delete=models.SET_NULL,null=True)
    subject = models.ForeignKey(SubjectModel,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.student} {self.subject}"

    class Meta:
        db_table = 'attendance'

class GradeModel(models.Model):
    student = models.ForeignKey(StudentModel,on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherModel,on_delete=models.SET_NULL,null=True)
    subject = models.ForeignKey(SubjectModel,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(default=datetime.now)
    mark = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.student} {self.subject} {self.mark}"

    class Meta:
        db_table = 'grade'
