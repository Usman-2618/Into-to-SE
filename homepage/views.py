from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from application import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login
from .tokens import generate_token

# Create your views here.
def enter(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request,'land.html')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('start')
    
    return render(request,'login.html')


    

def start(request):
    return render(request,'start.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        
        if not username:
            messages.error(request, "Username is required!")
            return redirect('register')
        
        if not email:
            messages.error(request, "Email is required!")
            return redirect('register')
        
        if not pass1:
            messages.error(request, "Password is required!")
            return redirect('register')
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('start')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('start')
        
        if len(username)>15:
            messages.error(request, "Username must be under 15 characters!!")
            return redirect('register')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created successfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email
        subject = "Welcome to Forkin fourtunate Login!!"
        message = "Hello there "  + "!!! \n" + "Welcome to our gang!! \n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nMuhammad Usman\nCeo @ Forkin Fourtunate"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ Forkin Fourtunate Login!!"
        message2 = render_to_string('activate.html',{
        
            'name': myuser.username,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('login')

    return render(request,'register.html')


def about(request):
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')

def land(request):
    return render(request,'land.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')

def booking(request):
    return render(request,'booking.html')

def order(request):
    return render(request,'menu1.html')

def contact(request):
    return render(request,'contact.html')

def checkoutpage(request):
    return render(request,'checkoutpage.html')

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
    return redirect('login')




