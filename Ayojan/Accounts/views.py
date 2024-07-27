from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from django.core.mail import send_mail,EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from . tokens import generate_token
from Ayojan import settings



#below funciton loads up profile_view html
def profile_view(request):

    return render(request, 'Accounts/profile_view.html')


#below funciton loads up login_page html
def login_view(request):
    if request.method == 'POST':
        #below the variable username and password store the values provided in login_page.html
        #under the input tage with name = 'USERNAME' and 'PASSWORD'
        username_or_email = request.POST['USERNAME_OR_EMAIL']
        password = request.POST['PASSWORD']

        user = authenticate(request, username = username_or_email, password = password)

        #check if the authenticate returns an object (if user exist) or None (if it doesn't)
        if user is not None:
            login(request, user)
            return redirect('mainpage:mainpage')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('Accounts:login_view')
    else:
        return render(request, 'Accounts\login_page.html')


#below funciton loads up signup_page html
def signup_view(request):
    #below i have taken the response provided by the user on the form and stored it an variable
    if request.method == "POST":
        username = request.POST['USERNAME']
        first_name = request.POST['FIRST_NAME']
        last_name = request.POST['LAST_NAME']
        email = request.POST['EMAIL']
        password = request.POST['PASSWORD']
        confirm_password = request.POST['CONFIRM_PASSWORD']

        #checking it password is equal confirm password
        if password != confirm_password:
            messages.error(request, "Password don't match")
            return redirect('Accounts:signup_view')

        # Checking if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exsist")
            return redirect('Accounts:signup_view')


        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exsist")
            return redirect('Accounts:signup_view')


        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.is_active = False
    
        myuser.save() 

        
        #Welcome Email
        subject = "Welcome to Ayojan"
        message = f"Hello, {first_name}!!\nYour Ayojan journey will be as smooth as possible.\nThank you for visiting our website.\nWe have sent you a confirmation email. Please check it.\n"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        

        #Confirmation Email

        current_site = get_current_site(request)
        email_subject = "Email Confirmation For Ayojan Website"
        message_2 = render_to_string('email_confirmation.html',{
            'name' : myuser.first_name,
            'domain' : current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token' : generate_token.make_token(myuser),
        })


        email = EmailMessage(
            email_subject,
            message_2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return render(request, 'Accounts\login_page.html')  
    else:
        return render(request, 'Accounts\signup_page.html')


def activate_acc(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.backend = 'django.contrib.auth.backends.ModelBackend' 
        myuser.is_active=True
        myuser.save()
        login(request,myuser,backend='django.contrib.auth.backends.ModelBackend')
        return redirect('mainpage:mainpage')
    else:
        return render(request,'activation_failed.html')



def signout(request):
    logout(request)
    return redirect('mainpage:mainpage')


def profile_info(request):
    return render(request, 'Accounts/personal_info.html')