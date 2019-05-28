from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs': blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id)) 

def fortune(request):
    fortuneRand = random.randrange(5) + 1
    if fortuneRand == 1:
        return HttpResponse("\nYou will receive a large some of money.")
    elif fortuneRand == 2:
        return HttpResponse("\nSomething you lost will soon turn up.")
    elif fortuneRand == 3:
        return HttpResponse("\nYou will have bad luck for a week.")
    elif fortuneRand == 4:
        return HttpResponse("\nToday is your lucky day!")
    elif fortuneRand ==5:
        return HttpResponse("\nYou will meet Mr. and Mrs. Right in 2 days!")