from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')


def post_job(request):
    return render(request,'post_job.html')


def join_now(request):
    return render(request,'join_now.html')


def find(request):
    return render(request,'find.html')        