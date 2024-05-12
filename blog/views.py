from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('hello world')

def post_list(request):
    return render(request, 'blog/post_list.html', {})

# Create your views here.
