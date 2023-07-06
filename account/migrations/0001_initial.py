# Generated by Django 3.2.20 on 2023-07-06 15:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=4)),
            ],
            options={
                'db_table': 'class',
            },
        ),
        migrations.CreateModel(
            name='ParentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('fname', models.CharField(default='', max_length=65)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('address', models.TextField()),
                ('user_name', models.CharField(default='', max_length=65)),
                ('password', models.CharField(default='', max_length=40)),
            ],
            options={
                'db_table': 'parent',
            },
        ),
        migrations.CreateModel(
            name='SchoolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(default=1)),
                ('address', models.CharField(default='', max_length=200)),
                ('info', models.JSONField()),
            ],
            options={
                'db_table': 'school',
            },
        ),
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=67)),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('fname', models.CharField(default='', max_length=65)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('address', models.TextField()),
                ('toifa', models.CharField(choices=[('OM', "Oliy Ma'lumot"), ('OR', "O'rta Ma'lumot"), ('OP', "O'qituvchi Pedagok")], default='', max_length=2)),
                ('salary', models.PositiveIntegerField(default=1)),
                ('school', models.ManyToManyField(to='account.SchoolModel')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.subjectmodel')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=65)),
                ('fname', models.CharField(default='', max_length=65)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('address', models.TextField()),
                ('user_name', models.CharField(default='', max_length=65)),
                ('password', models.CharField(default='', max_length=40)),
                ('avtive', models.BooleanField(default=True)),
                ('phone', models.CharField(default='', max_length=13)),
                ('clasS', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.classmodel')),
                ('parents', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.parentsmodel')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.schoolmodel')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='GradeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('mark', models.PositiveSmallIntegerField(default=1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.studentmodel')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.subjectmodel')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.teachermodel')),
            ],
            options={
                'db_table': 'grade',
            },
        ),
        migrations.CreateModel(
            name='AttendanceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.studentmodel')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.subjectmodel')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.teachermodel')),
            ],
            options={
                'db_table': 'attendance',
            },
        ),
    ]