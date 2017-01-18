from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import csv
import json
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html')


def blog_index(request):
    return render(request, 'blog.html')
