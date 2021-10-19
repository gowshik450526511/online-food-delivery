from django.shortcuts import render
from restaurant_app.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import south_breakfast
from .models import north_breakfast
from .models import north_lunch
from .models import south_lunch
from .models import south_dinner
from .models import north_dinner
from .models import orders

# Create your views here.
def index(request):
    return render(request,'restaurant_app/index.html')

def home(request):
    return render(request,'restaurant_app/home.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in,Nice!")

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else :
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'restaurant_app/registration.html',
                            {'user_form':user_form,
                              'profile_form':profile_form,
                              'registered':registered})

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not activated")

        else:
            print("Someone tried to login your account")
            print("they tried with this login id {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'restaurant_app/login.html', {})

def south_indian_food(request):
    return render(request,'restaurant_app/south_indian_food.html')

def north_indian_food(request):
    return render(request,'restaurant_app/north_indian_food.html')

def south_indian_breakfast(request):
    about=south_breakfast.objects.all()
    return render(request,'restaurant_app/south_indian_breakfast.html',{'about':about})

def south_indian_lunch(request):
    about=south_lunch.objects.all()
    return render(request,'restaurant_app/south_indian_lunch.html',{'about':about})

def south_indian_dinner(request):
    about=south_dinner.objects.all()
    return render(request,'restaurant_app/south_indian_dinner.html',{'about':about})

def north_indian_breakfast(request):
    about=north_breakfast.objects.all()
    return render(request,'restaurant_app/north_indian_breakfast.html',{'about':about})

def north_indian_lunch(request):
    about=north_lunch.objects.all()
    return render(request,'restaurant_app/north_indian_lunch.html',{'about':about})

def north_indian_dinner(request):
    about=north_dinner.objects.all()
    return render(request,'restaurant_app/north_indian_dinner.html',{'about':about})

def ordered_item(request):
    return render(request,'restaurant_app/ordered_item.html')

def order(request):
    Add=""
    street_name=""
    phone_no=""
    customer_name=""
    if request.method == "POST":
        Add = request.POST['address']
        street_name = request.POST['street_name']
        phone_no = request.POST['phone_no']
        customer_name = request.user.username
    orders.objects.create(Address=Add,street_name=street_name,phone_no=phone_no,customer_name=customer_name);
    return render(request,'restaurant_app/orders.html')
