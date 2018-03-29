# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from django.utils.crypto import get_random_string

# Create your views here.


def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
        request.session['unique_id'] = get_random_string(length=14)
        print request.session['unique_id']
    return render(request, 'words/index.html')

def reset(request):
    del request.session['counter']
    del request.session['unique_id']
    return redirect('/')