from django.shortcuts import render

# Create your views here.

def pro_list(request):
    return render(request, 'pro_list.html')

def pro_info(request):
    return render(request, 'pro_info.html')