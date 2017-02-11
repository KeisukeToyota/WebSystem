from django.shortcuts import render
from .models import *
import re
import base64
import cv2
import cnn.deeplearning as dl
import numpy as np
# Create your views here.


def index(request):
    return render(request, 'cnn.html')


def getImage(request):
    datauri = request.POST['img']
    img_str = re.search(r'base64,(.*)', datauri).group(1)
    nparr = np.fromstring(base64.b64decode(img_str), np.uint8)
    img_src = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_negaposi = 255 - img_src
    img_gray = cv2.cvtColor(img_negaposi, cv2.COLOR_BGR2GRAY)
    thresh = 100
    max_pixel = 255
    ret, img_dst = cv2.threshold(img_gray,
                                 thresh,
                                 max_pixel,
                                 cv2.THRESH_BINARY)
    img_resize = cv2.resize(img_dst,(28,28))
    answer = dl.identification(img_resize)
    return render(request, 'cnn.html', {'answer':answer})
