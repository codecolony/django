from django.shortcuts import render, loader, RequestContext
from django.http import HttpResponse, Http404

import subprocess as sp

from .models import SayHello

# Create your views here.
def index(request):
    latest_name_list = SayHello.objects.order_by('-person_name')[:5]
    context = {'latest_name_list': latest_name_list}
    return render(request, 'sayhello/index.html', context)

def detail(request, name_id):
    person_name = get_object_or_404(SayHello, pk=name_id)
    return render(request, 'sayhello/detail.html', {'person_name': person_name})

def execpy(request):
    op_txt = sp.check_output(["python", "hello.py"])
	# op_txt = sp.check_output(["ping", "-c", "3", "localhost"])
    return render(request, 'sayhello/execpy.html', {'op_txt': op_txt})

def classfy(request):
    op_txt = sp.check_output(["python", "classfy.py"])
    # op_txt = sp.check_output(["ping", "-c", "3", "localhost"])
    return render(request, 'sayhello/execpy.html', {'op_txt': op_txt})