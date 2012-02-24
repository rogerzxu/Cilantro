# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from mysite.polls.models import Poll
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #t = loader.get_template('/root/mysite/templates/polls/index.html')
    #c = Context({
    #    'latest_poll_list': latest_poll_list,
    #})
    #return HttpResponse(t.render(c))
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('/home/project/mysite/templates/polls/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    #return HttpResponse("You're looking at poll %s." % poll_id)
    #try:
    #    p = Poll.objects.get(pk=poll_id)
    #except Poll.DoesNotExist:
    #    raise Http404
    #return render_to_response('/root/mysite/templates/polls/detail.html', {'poll': p})
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('/home/project/mysite/templates/polls/detail.html', {'poll': p})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

