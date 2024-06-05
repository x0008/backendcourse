from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("<h1>Hello Mr.cool</h1>")
    people = ["aman","nameet","bubu"]
    return render(request,"index.html",context={'peoples':people})