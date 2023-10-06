from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login

from django.shortcuts import render,redirect
from chat.models import Customers,UserProfile,Message
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from chat.serializers import MessageSeriallizer
from .register import RegisterUser
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from chat.views import getuserid
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

@csrf_exempt
def social_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')    
        fields = RegisterUser(name=name, username=username, email=email, password=password, confirm_password=password)
        emails = fields.validate_email()
        usernames = fields.validate_username()
        password = fields.validate_password()
        if not emails:
            print("Email already registered!")
        elif not usernames:
            print("Username already registered!")
        return render(request,'project/post/home.html')
    return render(request,'project/post/home.html')

def project_view(request):
    return render(request,'project/post/projects.html')

def dashboard(request):
    if User.is_authenticated:
        return render(request,'project/post/dashboard.html')
    else:
        return redirect("login/")        
    
@sensitive_post_parameters('pswd', 'cpswd')
def user_register(request):
    """Registers a User"""
    message=[]
    if request.method == 'POST':
        body = request.POST

        name=body.get('name')
        username=body.get('username')
        email=body.get('email')
        password=body.get('pswd')
        confirm_password=body.get('cpswd')

        fields = RegisterUser(name=name, username=username, email=email, password=password, confirm_password=confirm_password)
        email = fields.validate_email()
        username = fields.validate_username()
        password = fields.validate_password()
        if not email:
            message.append("Email already registered!")
        elif not username:
            message.append("Username already registered!")
        elif not password:
            message.append("Passwords don't match!")
        else:
            print("SUCCESS!!!!")
            fields.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            profile = UserProfile(email=email, name=name, username=username)
            profile.save()
            return redirect("dashboard/")

    return render(request, 'project/post/register.html', {"message": message})

    
@sensitive_post_parameters('pswd')
def user_login(request):
    """Handles User Login"""
    message = []
    if request.method == 'POST':
        body = request.POST
        name = body.get('username',False)
        password = body.get('pswd',False)

        if name:
            message.append("Username required!")
        elif password:
            message.append("Password required!")
        try:
            user = authenticate(name=name, password=password)
            login(request, user)
            return redirect('dashboard/')
        except:
            return render(request,'project/post/login.html',{"message":"invalid credential"})

    return render(request, 'project/post/login.html')
    
def forgot_password(request):
    message=[]
    if request.method == 'POST':
        body = request.POST
        email = body.get('email', False)

        confirm_email = UserProfile.objects.filter(Q(email=email))
        if confirm_email.exists():
            for email in confirm_email:
                subject = "Password Reset Requested"
                email_template_name = "project/post/reset_password_complete.html"
                c = {
                    "email":email.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(email.pk)),
                    "email": email,
                    'token': default_token_generator.make_token(email),
                    'protocol': 'http',
                }
                email = render_to_string(email_template_name, c)
                try:
                    send_mail(subject, email, 'admin@example.com' , [email.email], fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect ("/password_reset_done")
    return render(request, "project/post/forgot_password.html")

def password_reset_done(request):
    return redirect(request,'project/post/password_reset_done.html')

def logout_view(request):
    logout(request)
    return redirect('/')

@csrf_exempt
def chatlogin(request):
  if request.POST.get('action') == 'chatlogin':
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    name = request.POST.get('name')    
    fields = RegisterUser(name=name, username=username, email=email, password=password, confirm_password=password)
    emails = fields.validate_email()
    usernames = fields.validate_username()
    password = fields.validate_password()
    if not emails:
        p="Email already registered!"
    elif not usernames:
        p="Username already registered!"
    data={data:p}
    return JsonResponse(data, safe=False)

# class PasswordChangeView(TemplateView):
#     url_name = 'password_reset_view'
#     template_name = 'project/post/forgot_password.html'
#     redirect('password_reset_done')

#     if request.method == 'POST':