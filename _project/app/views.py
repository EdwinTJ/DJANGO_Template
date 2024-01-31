from django.shortcuts import render
from django.http import HttpRequest
import string
import random
# Create your views here.
def index(request : HttpRequest):
    return render(request,"app/index.html")

def passwords(request: HttpRequest):
    query = request.GET
    length = int(query.get("length",10))
    count = int(query.get("count",1))
    passwords = []
    letters = string.ascii_letters + string.digits

    for _ in range(count):
        password = "".join(random.choice(letters) for _ in range(length))
        passwords.append(password)
    print(passwords)
    context ={
        "passwords":passwords
    }
    return render(request,"app/passwords.html",context)