from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from .models import Session


class SessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        # Read the session token from the cookie
        session_token = request.COOKIES.get('session_token')

        # Find the sessions by their token
        sessions = Session.objects.filter(token=session_token)

        if sessions.exists():
            # print("Session exists inside middleware")
            # Use the first session if there are multiple sessions with the same token
            session = sessions.last()
            request.user = session.user
            request.is_authenticated = True  # Set is_authenticated attribute
        else:
            # print("Session does not exist inside middleware")
            request.user = None
            request.is_authenticated = False  # Set is_authenticated attribute

        # Call the next middleware and return the result
        response = self.get_response(request)
        return response
    
    def requires_login(self, path):
        # List of URIs that require the user to be logged in
        login_required_uris = ['/destinations/', '/destinations/new/',
                               '/destinations/<int:destination_id>/',
                               '/destinations/<int:destination_id>/destroy/']

        return path in login_required_uris
