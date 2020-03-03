from django.shortcuts import render, redirect
from dappx.forms import UserForm, RecordsForm
# from .models import AddAccount
# UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import NewAccount

# Create your views here.

def index(request):
    return render(request,'dappx/index.html')

def about(request):
    return render(request,'dappx/about.html')
    
def contact(request):
    return render(request,'dappx/contact.html')

@login_required
def dashboard(request):
    return render(request,'dappx/dashboard.html')

@login_required
def records(request):   
    return render(request,'dappx/records.html')

def status(request):
    recordsData = dappx_newaccount.objects.all()
    context = {'records': recordsData}
    return render(request,'status.html', context)

@login_required
def accounts(request):
    return render(request,'dappx/accounts.html')

@login_required
def addaccount(request):           
    R_Form= RecordsForm(request.POST or None)
    if request.method == 'POST':
        R_Form=RecordsForm(data=request.POST)
        if R_Form.is_valid():
            user = R_Form.save(commit='True')
            # Hash the password
            R_Form = RecordsForm()
            messages.success(request,'Employee record added successfully.')
        else:
            print("The details you entered are invalid. Please try again.")
    return render(request, 'dappx/add-account.html', {'RecordsForm': R_Form})

@login_required
def editaccount(request):
    return render(request,'dappx/edit-account.html')

def editaccount(request):
    return render(request,'dappx/edit-account.html')
    
@login_required
def special(request):
    return HttpResponse("You have logged in successfully!")
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user( username=username, email=email, password=password )
        user.save()
        print( "User created successfully." )
        return redirect( 'dappx:user_login' )
    else:
        return render( request, 'dappx/registration.html' )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'dappx/dashboard.html')
            else:
                return HttpResponse("Your account is inactive. Please contact the system administrator.")
        else:
            messages.error(request,'The login details you entered are invalid. Please try again.')
            # messages.error(request, 'Please contact system administrator.', extra_tags='forgot')
            return render(request, 'dappx/login.html')
    else:
        return render(request, 'dappx/login.html', {})

def custom_login(request):
    if request.user.is_authenticated():
        return render(request,'dappx/dashboard.html')
    else:
        return login(request)

# def permission_denied(request):
#         return render(request, 'dappx/403.html', context)

def table(request):
    newaccount_Data=NewAccount.objects.all()
    context = {'newaccount_Data' : newaccount_Data}
    return render(request, 'dappx/records.html', context)

def line_chart(request):
    line_chart = TemplateView.as_view(template_name='line_chart.html')
    line_chart_json = LineChartJSONView.as_view()