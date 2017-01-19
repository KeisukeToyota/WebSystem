from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import csv
import json
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.


def index(request):
    blog = Blog.objects
    return render(request, 'index.html', {'blog': blog})


def blog_index(request, id):
    blog = Blog.objects.get(id=id)
    comments = Comment.objects.filter(blog_id=id)
    return render(request, 'blog.html', {'blog': blog, 'comments':comments})


def post_comment(request, id):
    comment = request.POST['comment']
    c = Comment(body=comment, blog_id=id)
    c.save()
    return redirect("/blog/"+id)
