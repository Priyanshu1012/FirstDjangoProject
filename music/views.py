from django.http import HttpResponse
from django.shortcuts import render

from .models import Register_form

def index(request):

    context ={}
    return render(request,'music/index.html', context)


def detail(request):
    template="music/index.html"
    context={}
    return render(request,template,context)

def submit(request):

    if request.method == 'POST':
        application = request.POST['Application no.']
        password = request.POST['password']
        security = request.POST['pin']

    data = Register_form(
        Application_no = application,
        password = request.POST['password'] ,
        security =  request.POST['pin']
    )
    data.save()

    return HttpResponse('Hey!!!! you have registered')

