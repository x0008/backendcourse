from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):

    context = {
        'variable': "this is sent"
    }
    return render(request,'index.html' , context)

def about(response):
    return HttpResponse("This is about page")


def services(response):
    return HttpResponse("This is service page")

def contact(response):
    return HttpResponse("This is contact page")
