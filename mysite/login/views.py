# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from mysite.polls.models import Poll
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    return HttpResponse("user; login");
