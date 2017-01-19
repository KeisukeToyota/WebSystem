from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import csv
import json
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import re
import base64
import random
import cv2
import cnn.deeplearning as dl

# Create your views here.


def index(request):
    return render(request, 'cnn.html')


def getImage(request):
    datauri = request.POST['img']
    imgstr = re.search(r'base64,(.*)', datauri).group(1)
    name = 'static/image/' + str(random.randint(0,999999)) + '.png'
    output = open(name, 'wb')
    output.write(base64.b64decode(imgstr))
    output.close()
    img_src = cv2.imread(name)
    img_negaposi = 255 - img_src
    img_gray = cv2.cvtColor(img_negaposi, cv2.COLOR_BGR2GRAY)
    thresh = 100
    max_pixel = 255
    ret, img_dst = cv2.threshold(img_gray,
                                 thresh,
                                 max_pixel,
                                 cv2.THRESH_BINARY)
    img_resize = cv2.resize(img_dst,(28,28))
    cv2.imwrite(name, img_resize)
    answer = dl.identification(name)

    # print(binary_img)
    return render(request, 'cnn.html', {'answer':answer})
