from django.shortcuts import render
from .forms import UserRegistration,CustomerRegistration

# Create your views here.
def index(request):
    return render(request, 'index.html')


def signin(request):
    UserReg = UserRegistration()
    CustReg = CustomerRegistration()
    return render(request,'signin.html',{"UserReg":UserReg,'CustReg':CustReg})


def signup(request):
    UserReg = UserRegistration()
    CustReg = CustomerRegistration()
    return render(request,'signup.html',{"UserReg":UserReg,'CustReg':CustReg})

def adminpage(request):
    return render(request,'adminindex.html')


def userHome(request):
    return render(request,'userHome.html')