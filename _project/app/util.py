from .models import Session,User
from django.shortcuts import redirect
import re

def authenticate(request, email, password):
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            return user
        else:
            return None
    except User.DoesNotExist:
        return None

def login(request, user):
    session = Session.objects.create(user=user)
    response = redirect('destinations')  
    response.set_cookie('session_token', session.token)
    return response

def logout(request):
    session_token = request.COOKIES.get('session_token')
    if session_token:
        Session.objects.filter(token=session_token).delete()
    response = redirect('index') 
    response.delete_cookie('session_token')
    return response

def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex,email)):
        return True
    else:
        return False

def check_passwordForm(password):
    return len(password) >= 8 and any(char.isdigit() for char in password)