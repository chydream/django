from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField('学生姓名', max_length=32)
    class Meta:
        db_table = 'grade_student'



class Grade(models.Model):
    # student_name = models.CharField('学生姓名', max_length=32)
    student = models.ForeignKey(Student, null=True, related_name='stu_grade')
    subject_name = models.CharField('科目',max_length=32)
    score = models.FloatField('分数', default=0)
    year = models.SmallIntegerField('年份')

    class Meta:
        db_table = 'grade'

    def __str__(self):
        return 'subject_name:{0},score:{1}'.format(self.subject_name, self.score)