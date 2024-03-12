# Create your views here.
from django.shortcuts import render, redirect
from .models import Destination, Session,User
from django.http import HttpResponse
from .util import authenticate, login, logout,check_email,check_passwordForm
import secrets
import string
def index(request):
    user_name = request.user.name if request.user else "Guest"
    destinations = Destination.objects.filter(share_publicly=True).order_by('-id')[:5]
    return render(request, 'app/index.html',{'destinations':destinations, 'user_name':user_name})

def create_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')

        if not check_email(email):
            return HttpResponse("Invalid email",status=404)
        
        if not check_passwordForm(password):
            error_message = 'Password must be at least 8 characters long and contain at least one digit'
            return render(request, 'app/new_user.html', {'error_message': error_message})
        
        try:
             # Create a new user instance
            user = User(email=email, name=name)

            # Set the password using the set_password method
            user.set_password(password)

            # Save the user
            user.save()

            # Print All Users
            all_users = User.objects.all()
            print("All Users:")
            for user in all_users:
                print(f"Name: {user.name}, Email: {user.email}")

            # Generate a random token string with a random length
            token_length = secrets.choice(range(20, 30))  
            token_characters = string.ascii_letters + string.digits + string.punctuation
            session_token = ''.join(secrets.choice(token_characters) for _ in range(token_length))
            
            # Create a session with the random token
            # Log in the newly created user
            login(request, user)
            session = Session.objects.create(user=user, token=session_token)

            # Redirect to the destinations page after successful login and session creation
            response = redirect('destinations')
            response.set_cookie('session_token', session.token)
            return response
        except Exception as e:
            # Handle any exceptions that may occur during user creation
            return HttpResponse(f"User creation failed: {e}",status=404)
    else:
        return render(request, 'app/new_user.html')

def create_session(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            response = login(request, user)
            return response
        else:
            return HttpResponse("Invalid credentials",status=404)
    else:
        return render(request, 'app/new_session.html')
    
def destroy_session(request):
    response = logout(request)
    return response

def destinations(request):
    if request.is_authenticated:
        user_destinations  = Destination.objects.filter(user=request.user)
        return render(request, 'app/destinations.html', {'destinations': user_destinations})
    else:
        return HttpResponse("You need to be logged in to view destinations")

def create_destination(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        review = request.POST.get('review')
        rating = request.POST.get('rating')

         # Check if share_publicly is received
        share_publicly = request.POST.get('share_publicly', False)
        # Convert string value to boolean
        share_publicly = share_publicly == 'true'
        destination = Destination.objects.create(user=request.user, name=name, review=review, rating=rating, share_publicly=share_publicly)
        return redirect("index")
    else:
        return render(request, 'app/new_destination.html')

def edit_destination(request, id):
    destination = Destination.objects.get(id=id)
    if request.method == 'POST':
        destination.name = request.POST.get('name')
        destination.review = request.POST.get('review')
        destination.rating = request.POST.get('rating')
        # Check if share_publicly is received
        share_publicly = request.POST.get('share_publicly', False)
        # Convert string value to boolean
        share_publicly = share_publicly == 'true'
        destination.share_publicly = share_publicly
        destination.save()
        return redirect("destinations")
    else:
        return render(request, 'app/edit_destination.html', {'destination': destination})

def destroy_destination(request, id):
    destination = Destination.objects.get(id=id)
    if request.method == 'POST':
        destination.delete()
        return redirect("index")
    else:
        return render(request, 'app/delete_destination.html', {'destination': destination})