from django.db.models import Sum, Max, Count
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from grade.models import Grade, Student


def page_count(request):
    # num = Grade.objects.filter(student_name= '张三').aggregate(total=Sum('score'))
    # print(num)
    # max_num = Grade.objects.filter(subject_name='语文').aggregate(high_score=Max('score'))
    # print(max_num)
    # sum_num = Grade.objects.values_list('student_name').annotate(Sum('score'))
    # print(sum_num)
    sum_num = Student.objects.all().annotate(Sum('stu_grade__score'))
    print(sum_num)
    for item in sum_num:
        print(item.student_name, item.stu_grade__score__sum)
    zs = Student.objects.get(pk=1)
    list = zs.stu_grade.all()
    print(list)
    return HttpResponse('ok')