from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django import template
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .models import Customer,User,EducationalResource,PlasticCollectionSchedule,PlasticCollection,Payment
from .forms import UserRegistration,CustomerRegistration
from datetime import datetime

# ------------------------------------------ Auth function start --------------------------------------

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user)
            if not user.is_user :
                user_data = Customer.objects.filter(user__id=user.id).first()
                print('User is:',user_data.approve)
                if user_data.approve == 'pending' or user_data.approve == 'disapproved':
                    messages.warning(request, 'Your account approval is pending or disapproved. Please wait for approval by the admin')
                    return render(request, 'signin.html')
                else:
                    request.session['user_id'] = user.id
                    return redirect('user_home')
            else:
                request.session['user_id'] = user.id
                return redirect('adminHomePage')
    return render(request,'signin.html')


def signup(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)
        customer_form = CustomerRegistration(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            print(request.FILES)
            if 'image' in request.FILES: 
                
                customer.image = request.FILES['image'] 
            customer.save()
            return redirect('signin')  
    else:
        UserReg = UserRegistration()
        CustReg = CustomerRegistration()

    return render(request, 'signup.html', {"UserReg":UserReg,'CustReg':CustReg})

def logout_view(request):
    logout(request)  # Logout the user
    request.session.clear()  # Clear session data
    return redirect('index') 
# ------------------------------------------ Auth function end --------------------------------------

def adminHomePage(request):
    user_id = request.session['user_id'] 
    print('User id is: ',user_id)
    admin = User.objects.filter(id=user_id)
    context = {
        'admin':admin
    }
    print(admin)

    return render(request,'admin_index.html',context)


def user_base(request):
    user_id = request.session['user_id'] 
    print('User id is: ',user_id)
    user = Customer.objects.filter(user__id=user_id)
    context = {
        'user':user
    }
    return render(request,'user_base.html',context)


def user_home(request):
    user_id = request.session['user_id'] 
    print('User id is: ',user_id)
    user = Customer.objects.filter(user__id=user_id)
    collections = PlasticCollectionSchedule.objects.all()
    contributions = PlasticCollection.objects.filter(user_id=user_id)
    print(contributions)
    context = {
        'user':user,
        'collections':collections,
        'contributions':contributions
    }
    return render(request,'user_home.html',context)


def Monitoring(request):
    return render(request,'MonitoringIndex.html')

def index(request):
    return render(request,'index.html')

def update_profile(request):
    user_id = request.session['user_id'] 
    
    user = Customer.objects.filter(user__id=user_id)
    context = {
        'user':user
    }
    if request.method == 'POST':
        user = Customer.objects.filter(user__id=user_id).first()
    
        # Check if 'image' key exists in request.FILES
        if 'image' in request.FILES:
            print('User image is: ',user.image)
            if user.image:
                user.image.delete() 
            user.image = request.FILES['image']
            user.save()
            
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        Customer.objects.filter(user__id=user_id).update(
            name=name,phone=phone,email=email
        )

       
    return render(request,'update_profile.html',context)


def users_list(request):
    users = Customer.objects.all()
    context = {
        'users':users
    }
    return render(request,'users_list.html',context)




def update_approval_status(request, user_id):
    if request.method == 'POST':
        data = request.POST  
        approval_status = data.get('approve')
        print(approval_status)
        Customer.objects.filter(user__id= user_id).update(approve=approval_status)
        return redirect('users_list')


def admin_view_users(request,user_id):
    user = Customer.objects.filter(user__id=user_id)
    context = {
        'user':user
    }
    if request.method == 'POST':
        user = Customer.objects.filter(user__id=user_id).first()
    
        # Check if 'image' key exists in request.FILES
        if 'image' in request.FILES:
            print('User image is: ',user.image)
            if user.image:
                user.image.delete() 
            user.image = request.FILES['image']
            user.save()
            
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        Customer.objects.filter(user__id=user_id).update(
            name=name,phone=phone,email=email
        )
    return render(request,'admin_view_users.html',context)


def educational_content_view(request):
    user_id = request.session['user_id'] 
    user = User.objects.filter(id=user_id).first()
    role = user.is_user
    print(role)
    contents = EducationalResource.objects.all()
    context = {
        'contents':contents,
        'role':role
    }
    return render(request,'educational_content_view.html',context)

def add_educational_content(request):
    if request.method == 'POST' and 'image' in request.FILES:
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES['image']
        EducationalResource.objects.create(title=title,content=content,image=image)
    return render(request,'add_educational_content.html')

def educational_content_view_user(request):
    user_id = request.session['user_id'] 
    user = User.objects.filter(id=user_id).first()
    users = Customer.objects.filter(user__id=user_id)
    role = user.is_user
    print(role)
    contents = EducationalResource.objects.all()
    context = {
        'contents':contents,
        'role':role,
        'user':users
    }
    return render(request,'educational_content_view_user.html',context)


def add_collection_shedule(request):
    user_id = request.session['user_id'] 
    
    user = Customer.objects.filter(user__id=user_id)
    context = {
        'user':user
    }
    if request.method == 'POST':
        user = Customer.objects.filter(user__id=user_id).first()
        place = request.POST.get('place')
        date = request.POST.get('date')
        time = request.POST.get('time')
        print(place,date,time)
        PlasticCollectionSchedule.objects.create(
            place=place,date=date,time=time
        )
    return render(request,'add_collection_shedule.html',context)

    

def admin_view_collection_shedule(request):
    collections = PlasticCollectionSchedule.objects.all()
    context = {
        'collections':collections
    }
    return render(request,'admin_view_collection_shedule.html',context)


def update_collection_schedule(request,collection_id):
    user_id = request.session['user_id'] 
    
    user = Customer.objects.filter(user__id=user_id)
    Schedule = PlasticCollectionSchedule.objects.filter(id=collection_id).first()
    context = {
        'user':user,
        'Schedule':Schedule
    }

    if request.method == 'POST':
        place = request.POST.get('place')
        date = request.POST.get('date')
        time = request.POST.get('time')
        print(place,date,time)
        formatted_date = datetime.strptime(date, '%Y-%m-%d').date()

        PlasticCollectionSchedule.objects.filter(id=collection_id).update(
            place=place,date=formatted_date,time=time
        )
        return redirect('admin_view_collection_shedule')
       
    return render(request,'update_collection_schedule.html',context)


def user_view_collection_shedule(request):
    user_id = request.session['user_id'] 
    print('User id is: ',user_id)
    user = Customer.objects.filter(user__id=user_id)

    schedules = PlasticCollectionSchedule.objects.all()
    context = {
        'user':user,
        'schedules':schedules,
    }
    
    return render(request,'user_view_collection_shedule.html',context)


def add_plastic_collection(request):
    user_id = request.session['user_id'] 
    
    user = Customer.objects.filter(user__id=user_id)
    users = Customer.objects.all()
    print(users)
    
    context = {
        'user':user,
        'users':users,
    }

    if request.method == 'POST':
        place = request.POST.get('place')
        date = request.POST.get('date')
        time = request.POST.get('time')
        selected_user = request.POST.get('user')
        collected_amount = request.POST.get('collected_amount')
        print(place,date,time)
        formatted_date = datetime.strptime(date, '%Y-%m-%d').date()

        PlasticCollection.objects.create(
            user_id=selected_user,
            place=place,date=formatted_date,time=time,amount_collected=collected_amount
        )
    return render(request,'add_plastic_collection.html',context)



def collected_plastic_details(request):
    user_id = request.session['user_id'] 
    print('User id is: ',user_id)
    user = Customer.objects.filter(user__id=user_id)

    collections = PlasticCollection.objects.all()
    context = {
        'user':user,
        'collections':collections,
    }
    
    return render(request,'collected_plastic_details.html',context)




def payment_list(request):
    user_id = request.session['user_id'] 
    print('User id is: ',user_id)
    user = Customer.objects.filter(user__id=user_id)
    contributions = PlasticCollection.objects.filter(user_id=user_id)
    print(contributions)
    context = {
        'user':user,
        'contributions':contributions
    }
  
    return render(request,'payment_list.html',context)


def payment_form(request,payment_id):
    user_id = request.session['user_id'] 
    print('User id is: ',user_id)
    user = Customer.objects.filter(user__id=user_id)
    contributions = PlasticCollection.objects.filter(id=payment_id).values()
    
        
    context = {
        'user':user,
        'contributions':contributions,
    }
  
    return render(request,'payment_form.html',context)

def payment_confirm(request,payment_id):
    user_id = request.session['user_id'] 
    if request.method == 'POST':
        cardNumber = request.POST.get('cardNumber')
        cardDate = request.POST.get('cardDate')
        cvc = request.POST.get('cvc')
        nameOnCard = request.POST.get('nameOnCard')
        streetAddress = request.POST.get('streetAddress')
        zipCode = request.POST.get('zipCode')
        Payment.objects.create(
            user_id=user_id,payment_id=payment_id,cardNumber=cardNumber,
            cardDate=cardDate,cvc=cvc,nameOnCard=nameOnCard,
            streetAddress=streetAddress,zipCode=zipCode
        )
        PlasticCollection.objects.filter(id=payment_id).update(payment_status='paid')


        return redirect('payment_success')
    
def payment_success(request):
    return render(request,'payment_success.html')