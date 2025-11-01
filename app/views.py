from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

PASSWORD = "mysecretpassword123" 
def authenticate(username, password):
    test = str()
    l = list()
    if username == "admin" and password == PASSWORD:
        return True
    return False