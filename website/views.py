# coding:utf-8
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from website.models import Article
import datetime

def home(request):
    post_list = Article.objects.all()
    return render(request, 'blog/home.html', {'post_list': post_list})

def Test(request):
    return render(request, 'blog/test.html', {'current_time': datetime.datetime.now()})

def Detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog/post.html', {'post': post})
