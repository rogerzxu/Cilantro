# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.contrib.auth import logout

def my_homepage_view(request):
    #html = "<html><a href = \"/login/\">Login</a></html>"
    #return HttpResponse(html)
    c = RequestContext(request)
    return render_to_response('index.html', c)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

#def image_page(request):
  #  html = "<html><img src = \"home/project/mysite/images/cilantro.jpg\" alt=\"Cilantro\" /></html>"
   # return HttpResponse(html)
