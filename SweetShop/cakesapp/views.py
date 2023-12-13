from django.shortcuts import render, redirect
import datetime
from .models import Cakes
from .models import Category
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def index(request):
    cakes = Cakes.objects.all()
    categories = Category.objects.all()
    context = {
        "cakes": cakes,
        "categories": categories,

    }
    return render(request, 'index.html', context)


# def category(request, category_id):
#     cakes = Cakes.objects.filter(category_id=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     context = {
#         "cakes": cakes,
#         "categories": categories,
#         "category": category
#     }
#     return render(request, 'category.html', context)
def get_category(request,category_id):

    cakes = Cakes.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context={
        'cakes':cakes,
        'categories':categories,
        'category':category,
    }
    return render(request, 'category.html', context)


def cakes(request):
    cakes = Cakes.objects.all()

    context = {
        'nkaragir': cakes,

    }
    return render(request, 'cakes.html', context)


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index:homepage")

    form = NewUserForm
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)


def login(request):
    if request.user.is_authenticated:
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('posts')  # profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, '/', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, '/', {'form': form})