from django.shortcuts import render,HttpResponse , redirect
from .models import *
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required

def new(request):
    return HttpResponse("Hello welcome")
# @login_required(login_url="/login/")
def main_page(request):

    if request.method == "POST":
        data = request.POST

        recipe_name1 = data.get('recipe_name')
        recipe_category1 = data.get('recipe_category')

        print(recipe_name1)
        print(recipe_category1)

        items.objects.create(
            recipe_name = recipe_name1,
            recipe_category = recipe_category1
        )
        return redirect('/receipe/')
    
    return render(request,'main_page.html')

def view_page(request):

    data = items.objects.all()

    context = {"recipes":data}

    return render(request,"view_page.html",context)

# def append_item(request):

def delete_recipe(request,id):
    data = items.objects.get(id=id)
    data.delete()

    return redirect("/getreceipe/")

def update_recipe(request,id):
    queryset = items.objects.get(id=id)

    context = {"recipes":queryset}

    if request.method == "POST":
        data = request.POST
        recipe_name1 = data.get('recipe_name')
        recipe_category1 = data.get('recipe_category')

        queryset.recipe_name = recipe_name1
        queryset.recipe_category = recipe_category1

        queryset.save()

        return redirect("/getreceipe/")
    
    return render(request,"update.html",context)


from django.contrib.auth import authenticate, login,logout


def login_page(request):

    if request.method == "POST":
        data = request.POST
        username = data.get("username1")
        password = data.get("password1")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
        # Redirect to a success page.
            return redirect('/receipe/')
        
        else:
        # Return an 'invalid login' error message.
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html')


def register(request):

    if request.method == "Post":
        # data = request.POST
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)
        # user = User.objects.filter(username = username)
        if User.objects.filter(username=username).exists():
        # if user.exists():
            return redirect('/register/')
        
        user = User.objects.create(
            username = username
            # password=password

        )
        user.set_password(password)
        user.save()

        return redirect('/login/')



    
    return render(request,'register.html')


def logout_page(request):
    logout(request)

    return redirect("/login/")